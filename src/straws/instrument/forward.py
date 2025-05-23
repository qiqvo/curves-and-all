from dataclasses import dataclass

from straws.data.utils import get_discount_curve
from straws.instrument.instrument import Instrument


@dataclass
class Forward(Instrument):
    strike: float
    forward_curve_id: str 
    discount_curve_id: str

    def price_internal(self, on_date):
        forward_curve = get_discount_curve(self.forward_curve_id)
        discount_curve = get_discount_curve(self.discount_curve_id)

        eq = forward_curve.discount_on_date(on_date, self.maturity)
        er = discount_curve.discount_on_date(on_date, self.maturity)

        return eq / er * self.strike