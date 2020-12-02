import attr
import typing 
import pandas as pd
import numpy as np

@attr.s(slots=True, auto_attribs=True)
class Interpolation(object):
	"""
	Abstract interpolation. 
	Elements:
		data
	"""
	data : pd.DataFrame = attr.ib(default=None)
		
	def value(self, time):
		times = self.data["Time"].values
		
		if time > times[-1]:
			i = -2
		else:
			# find interval
			i = 0
			while time > times[i]:
				i += 1
			i -= 1

		v1 = self.data.iloc[i]["Value"]
		v2 = self.data.iloc[i + 1]["Value"]
		
		return self.interpolate(time, times[i], times[i+1], v1, v2)

	@staticmethod
	def interpolate(time, time1, time2, value1, value2):
		"""Given value1 at time1 and value2 at time2 interpolate for time."""
		return None

@attr.s(slots=True, auto_attribs=True)
class LinearInterpolation(Interpolation):
	"""
	Linear interpolation
	"""
	@staticmethod
	def interpolate(time, time1, time2, value1, value2):
		c = time2 - time1
		return (time2 - time) / c * value1 + value2 * (time - time1) / c 

@attr.s(slots=True, auto_attribs=True)
class LogLinearInterpolation(Interpolation):
	"""
	Log linear interpolation
	"""
	@staticmethod
	def interpolate(time, time1, time2, value1, value2):
		value1 = np.log(value1)
		value2 = np.log(value2)

		log_scale = LinearInterpolation.interpolate(time, time1, time2, value1, value2)
		return np.exp(log_scale)