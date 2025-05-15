from dataclasses import dataclass

from straws.curve.discount_curve import DiscountCurve
from straws.instrument.instrument import Instrument


@dataclass
class Forward(Instrument):
    strike: float
    forward_curve_id: str 
    discount_curve_id: str

    def _price(self, time=0):
        forward_curve = DiscountCurve.load(self.forward_curve_id)
        discount_curve = DiscountCurve.load(self.discount_curve_id)

        eq = forward_curve.discount(self.maturity) / forward_curve.discount(time)
        er = discount_curve.discount(self.maturity) / discount_curve.discount(time)

        return eq / er * self.strike