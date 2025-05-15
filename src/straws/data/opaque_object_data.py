from dataclasses import dataclass, asdict

from straws.data.object_data import ObjectData
from straws.data.object_registry import ObjectRegistry

@dataclass
class OpaqueObjectData(ObjectData):
    """
    OpaqueObjectData is a subclass of ObjectData that allows for saving and loading
    of objects with a specific type and data. It uses the ObjectRegistry to manage
    the storage and retrieval of these objects.

    Opaque because it does not store the object itself, 
    but rather the type and data of the object.
    """

    def save(self):
        ObjectRegistry.save(self.id, (type(self), asdict(self)))

    @classmethod
    def load(cls, id):
        type, data = ObjectRegistry.load(id)
        return type(**data)
