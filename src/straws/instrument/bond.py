from dataclasses import dataclass
from typing import List

import pandas as pd

from straws.curve.basis import Basis, resolve_basis
from straws.curve.discount_curve import DiscountCurve
from straws.instrument.instrument import Instrument
from straws.settings import Settings


@dataclass
class Bond(Instrument):
    coupon: float
    coupon_dates: List[str]
    basis_type: str
    discount_curve_id: str

    def price_internal(self, on_date=0):
        discount_curve: DiscountCurve = DiscountCurve.load(self.discount_curve_id)

        res = 0
        for d in self.coupon_dates:
            if d < on_date:
                continue
            else:
                res += self.coupon * discount_curve.evaluate_on_date(d) / discount_curve.evaluate_on_date(on_date)
            
        res += discount_curve.evaluate_on_date(self.maturity) / discount_curve.evaluate_on_date(on_date)

        return res