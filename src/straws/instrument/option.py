from abc import abstractmethod
import attr
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from straws.curve.discount_curve import DiscountCurve
from straws.instrument.instrument import Instrument
from straws.model.model import Model


@attr.s(slots=True, auto_attribs=True)
class Option(Instrument):
    flavour: str = attr.ib(default=None)
    notional: float = attr.ib(default=None)
    currency: str = attr.ib(default=None)
    model_id: str = attr.ib(default=None)
    strike: float = attr.ib(default=None)
    discount_curve_id: str = attr.ib(default=None)

    def _price(self, time):
        model = Model.load(self.model_id)
        return model.price_option(self, self.strike, self.maturity, self.flavour, time)
        
    def payoff(self, value, time):
        curve = DiscountCurve.load(self.discount_curve_id)
        discount = curve.discount(self.maturity) / curve.discount(time)
        
        res = (value - self.strike) * self.notional * discount
        if self.flavour == 'put':
            res = -res
        if res < 0:
            res = 0
        return res