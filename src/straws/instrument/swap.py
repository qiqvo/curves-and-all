from abc import abstractmethod
from dataclasses import dataclass
from typing import List

import pandas as pd

from straws.curve.basis import Basis, resolve_basis
from straws.curve.discount_curve import DiscountCurve
from straws.instrument.instrument import Instrument
from straws.instrument.swap_legs.base_leg import BaseLeg
from straws.settings import Settings


@dataclass
class Swap(Instrument):
    strike: float
    fixed_rate: float
    basis_type_fixed: str 
    swap_dates: List[str]
    floating_curve_id: str 
    discount_curve_id: str

    def __post_init__(self):
        self.basis : Basis = Instrument.get_basis(self.basis_type_fixed)
        # self.swap_times = pd.to_datetime(self.swap_dates)
        # self.swap_times = self.swap_times.map(lambda x: self.basis.get_time(x))
        self.legs = self.get_legs()

    @abstractmethod
    def get_legs(self) -> List[BaseLeg]:
        raise NotImplementedError("Subclasses must implement this method.")

    def price_internal(self, on_date=0):
        res = sum([leg.price_internal(on_date) for leg in self.legs])
        return res
    
        floating_curve:DiscountCurve = DiscountCurve.load(self.floating_curve_id)
        discount_curve:DiscountCurve = DiscountCurve.load(self.discount_curve_id)

        res = 0
        prev_d = on_date
        for d in self.swap_dates:
            if d < on_date:
                continue
            else:
                a = floating_curve.discount(t) / floating_curve.evaluate_on_date(on_date)
                a -= self.fixed_rate
                res += a * self.basis.get_delta(prev_d, d) * discount_curve.evaluate_on_date(d) / discount_curve.evaluate_on_date(on_date)
            
            prev_d = d
        return res

@dataclass
class VanillaSwap(Swap):