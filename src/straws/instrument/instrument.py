from abc import abstractmethod
from dataclasses import dataclass

import pandas as pd

from straws.data.opaque_object_data import OpaqueObjectData


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
    