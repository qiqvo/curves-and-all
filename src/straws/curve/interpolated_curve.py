from dataclasses import dataclass
from typing import * 
import pandas as pd
import numpy as np

import matplotlib.pyplot as plt

from straws.curve.curve import Curve
from straws.curve.interpolation import Interpolation, resolve_interpolation
from straws.data.utils import get_basis

@dataclass
class InterpolatedCurve(Curve):
	dates: List[str] 
	values: List[float] 
	interpolation_type: str 

	def __post_init__(self):
		self.basis = get_basis(self.basis_type)
		self.set_times()
		self.set_interpolation()

	def set_times(self):
		pd_dates = pd.to_datetime(self.dates)
		self.times = pd_dates.map(lambda x: self.basis.get_time(x))

	def set_interpolation(self):
		self.interpolation : Interpolation = resolve_interpolation(self.interpolation_type, self.times, self.values)

	def evaluate(self, time : float):
		return self.interpolation.value(time)

	def plot(self):
		times = np.linspace(self.times[0], self.times[-1], 100)
		
		plt.plot(times, [self.evaluate(t) for t in times])
		plt.scatter(self.times, self.values, c='r')
		# plt.show()
