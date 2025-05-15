from abc import abstractmethod
from dataclasses import dataclass

import pandas as pd

from straws.data.opaque_object_data import OpaqueObjectData


@dataclass
class Instrument(OpaqueObjectData):
    name: str
    maturity: pd.Timestamp
    notional: float
    currency: str

    @abstractmethod
    def _price(self, time):
        raise NotImplementedError("Price method not implemented for this instrument")

    def price(self, time):
        return self._price(time) * self.notional