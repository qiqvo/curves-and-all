from abc import abstractmethod
from dataclasses import dataclass

import pandas as pd

from straws.data.opaque_object_data import OpaqueObjectData
from straws.settings import Settings


@dataclass
class Instrument(OpaqueObjectData):
    maturity: pd.Timestamp
    notional: float
    currency: str

    @abstractmethod
    def price_internal(self, on_date):
        raise NotImplementedError("Price method not implemented for this instrument")

    def price(self, on_date):
        return self.price_internal(on_date) * self.notional
    
    @staticmethod
    def get_discount_curve(discount_curve_id):
        from straws.curve.discount_curve import DiscountCurve
        return DiscountCurve.load(discount_curve_id)

    @staticmethod
    def get_basis(basis_type):
        from straws.curve.basis import resolve_basis
        today = Settings.get_active_settings().today
        return resolve_basis(basis_type, today)