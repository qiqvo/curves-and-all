import uuid

class ObjectRegistry:
    _objects = {}
    active_settings_id = None

    @staticmethod
    def create_id():
        """Generate a unique ID for an object."""
        return str(uuid.uuid4())

    @classmethod
    def save(cls, key, data):
        cls._objects[key] = data

    @classmethod
    def load(cls, key):
        data = cls._objects.get(key)
        if data is None:
            raise KeyError(f"No object found with key '{key}'")
        return data
    
    @staticmethod
    def activate_settings(settings):
        ObjectRegistry.active_settings_id = settings.id
        settings.save()
    
    @staticmethod
    def get_active_settings_id():
        return ObjectRegistry.active_settings_id