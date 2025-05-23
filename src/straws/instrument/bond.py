from dataclasses import dataclass
from typing import List

import pandas as pd

from straws.data.utils import get_basis, get_discount_curve
from straws.instrument.instrument import Instrument


@dataclass
class Bond(Instrument):
    coupon: float
    coupon_dates: List[str]
    basis_type: str
    discount_curve_id: str

    def __post_init__(self):
        self.basis = get_basis(self.basis_type)
        self.discount_curve = get_discount_curve(self.discount_curve_id)

    def price_internal(self, on_date: pd.Timestamp) -> float:
        res = 0
        for d in self.coupon_dates:
            if d < on_date:
                continue
            else:
                res += self.coupon * self.discount_curve.discount_on_date(on_date, d)
        res += self.discount_curve.discount_on_date(on_date, self.maturity)

        return res