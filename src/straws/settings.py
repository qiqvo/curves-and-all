
from dataclasses import dataclass

import pandas as pd

from straws.data.object_registry import ObjectRegistry
from straws.data.opaque_object_data import OpaqueObjectData


@dataclass
class Settings(OpaqueObjectData):
    today : pd.Timestamp
    # discount_curve_id : str

    def activate(self):
        ObjectRegistry.activate_settings(self)

    @staticmethod
    def get_active_settings():
        return Settings.load(ObjectRegistry.get_active_settings_id())