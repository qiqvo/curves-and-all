from abc import abstractmethod
from dataclasses import dataclass
from typing import List, Tuple

import pandas as pd

from straws.instrument.instrument import Instrument
from straws.instrument.swap_legs.base_leg import BaseLeg
from straws.instrument.swap_legs.fixed_leg import FixedLeg
from straws.instrument.swap_legs.float_leg import FloatLeg


@dataclass
class Swap(Instrument):
    strike: float
    fixed_rate: float
    basis_type_leg_1: str 
    basis_type_leg_2: str 
    swap_dates: List[str]
    floating_curve_id: str 
    discount_curve_id: str

    def __post_init__(self):
        self.legs = self.get_legs()

    @abstractmethod
    def get_legs(self) -> List[BaseLeg]:
        raise NotImplementedError("Subclasses must implement this method.")

    def price_internal(self, on_date: pd.Timestamp) -> float:
        return sum([sign * leg.price_internal(on_date) for sign, leg in self.legs])
    
@dataclass
class VanillaSwap(Swap):
    notional: float
    currency: str
    maturity: pd.Timestamp

    def get_legs(self) -> List[Tuple[int, BaseLeg]]:
        legs = []
        leg1 = FixedLeg(
            notional=self.notional,
            currency=self.currency,
            maturity=self.maturity,
            fixed_rate=self.fixed_rate,
            basis_type=self.basis_type_leg_1,
            swap_dates=self.swap_dates,
            discount_curve_id=self.discount_curve_id
        )
        leg2 = FloatLeg(
            notional=self.notional,
            currency=self.currency,
            maturity=self.maturity,
            basis_type=self.basis_type_leg_2,
            floating_curve_id=self.floating_curve_id,
            swap_dates=self.swap_dates,
            discount_curve_id=self.discount_curve_id
        )
        legs.append((1, leg1))
        legs.append((-1, leg2))
        return legs