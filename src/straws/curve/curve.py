from abc import abstractmethod
from dataclasses import dataclass

from straws.curve.basis import Basis, resolve_basis
from straws.data.opaque_object_data import OpaqueObjectData
from straws.settings import Settings

@dataclass
class Curve(OpaqueObjectData):
	basis_type: str 

	def __post_init__(self):
		self.set_basis()
	
	def set_basis(self):
		today = Settings.get_active_settings().today
		self.basis : Basis = resolve_basis(self.basis_type, today)

	@abstractmethod
	def evaluate(self, time : float):
		raise NotImplementedError("Subclasses must implement this method.")
	
	def evaluate_on_date(self, date):
		time = self.basis.get_time(date)
		return self.evaluate(time)

	@abstractmethod
	def plot(self):
		raise NotImplementedError("Subclasses must implement this method.")