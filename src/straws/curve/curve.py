import attr
from typing import * 
import pandas as pd
import numpy as np

import matplotlib.pyplot as plt

from straws.curve.interpolation import Interpolation

@attr.s(slots=True, auto_attribs=True)
class Curve():
	times : List[float] = attr.ib(default=None)
	data : List[float] = attr.ib(default=None)
	interpolation : Interpolation = attr.ib(default=None)

	def value(self, time : float):
		return self.interpolation.value(time)

	def values(self, times : List[float]):
		return np.array([self.value(time) for time in times])

	def plot(self):
		times = np.linspace(self.times[0], self.times[-1], 100)
		
		plt.plot(times, self.values(times))
		plt.scatter(self.times, self.data, c='r')
		# plt.show()
