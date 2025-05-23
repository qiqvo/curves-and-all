from dataclasses import dataclass

from straws.data.utils import get_basis, get_discount_curve
from straws.instrument.instrument import Instrument

@dataclass
class BaseLeg(Instrument):
    basis_type: str
    swap_dates: list
    discount_curve_id: str 

    def __post_init__(self):
        self.basis = get_basis(self.basis_type)
        self.discount_curve = get_discount_curve(self.discount_curve_id)