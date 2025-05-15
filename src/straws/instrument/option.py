from dataclasses import dataclass

from straws.curve.discount_curve import DiscountCurve
from straws.instrument.instrument import Instrument
from straws.model.model import Model


@dataclass
class Option(Instrument):
    flavour: str 
    notional: float 
    currency: str 
    model_id: str  
    strike: float  
    discount_curve_id: str  

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