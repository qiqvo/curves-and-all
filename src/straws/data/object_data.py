from abc import abstractmethod
from dataclasses import KW_ONLY, InitVar, dataclass, field
import uuid

@dataclass
class ObjectData(object):
    _: KW_ONLY
    id: str = field(default_factory=lambda: str(uuid.uuid4()))

    @abstractmethod
    def save(self):
        raise NotImplementedError("Save method not implemented for this object")

    @classmethod
    @abstractmethod
    def load(cls, id):
        raise NotImplementedError("Load method not implemented for this object")
