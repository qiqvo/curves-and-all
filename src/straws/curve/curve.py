from abc import abstractmethod
from dataclasses import dataclass

from straws.data.opaque_object_data import OpaqueObjectData
from straws.data.utils import get_basis

@dataclass
class Curve(OpaqueObjectData):
	basis_type: str 

	def __post_init__(self):
		self.basis = get_basis(self.basis_type)

	@abstractmethod
	def evaluate(self, time : float):
		raise NotImplementedError("Subclasses must implement this method.")
	
	def evaluate_on_date(self, date):
		time = self.basis.get_time(date)
		return self.evaluate(time)

	@abstractmethod
	def plot(self):
		raise NotImplementedError("Subclasses must implement this method.")