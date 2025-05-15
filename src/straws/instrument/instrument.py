from abc import abstractmethod
import attr

from straws.data.opaque_object_data import OpaqueObjectData


@attr.s(slots=True, auto_attribs=True)
class Instrument(OpaqueObjectData):
    name: str = attr.ib(default=None)
    maturity: float = attr.ib(default=None)
    notional: float = attr.ib(default=None)
    currency: str = attr.ib(default=None)

    @abstractmethod
    def _price(self, time):
        raise NotImplementedError("Price method not implemented for this instrument")

    def price(self, time):
        return self._price(time) * self.notional