import attr

from straws.data.object_data import ObjectData
from straws.data.object_registry import ObjectRegistry


class PureObjectData(ObjectData):
    def save(self):
        ObjectRegistry.save(self.id, self)

    @classmethod
    def load(cls, id):
        data = ObjectRegistry.load(id)
        return data

