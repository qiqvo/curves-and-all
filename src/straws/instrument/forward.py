from abc import abstractmethod
import attr
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from straws.curve.discount_curve import DiscountCurve
from straws.instrument.instrument import Instrument


@attr.s(slots=True, auto_attribs=True)
class Forward(Instrument):
    strike: float = attr.ib(default=None)
    forward_curve_id: str = attr.ib(default=None)
    discount_curve_id: str = attr.ib(default=None)

    def _price(self, time=0):
        forward_curve = DiscountCurve.load(self.forward_curve_id)
        discount_curve = DiscountCurve.load(self.discount_curve_id)

        eq = forward_curve.discount(self.maturity) / forward_curve.discount(time)
        er = discount_curve.discount(self.maturity) / discount_curve.discount(time)

        return eq / er * self.strike