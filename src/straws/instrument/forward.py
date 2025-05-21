from dataclasses import dataclass

from straws.curve.discount_curve import DiscountCurve
from straws.instrument.instrument import Instrument


@dataclass
class Forward(Instrument):
    strike: float
    forward_curve_id: str 
    discount_curve_id: str

    def price_internal(self, on_date):
        forward_curve:DiscountCurve = DiscountCurve.load(self.forward_curve_id)
        discount_curve:DiscountCurve = DiscountCurve.load(self.discount_curve_id)

        eq = forward_curve.evaluate_on_date(self.maturity) / forward_curve.evaluate_on_date(on_date)
        er = discount_curve.evaluate_on_date(self.maturity) / discount_curve.evaluate_on_date(on_date)

        return eq / er * self.strike