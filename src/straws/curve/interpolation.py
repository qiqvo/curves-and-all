from typing import * 
import numpy as np


class Interpolation(object):
	"""
	Abstract interpolation. 
	Elements:
		data
	"""
	def __init__(self, times:List[float], values:List[float]):
		self.times = times
		self.values = values
		
	def value(self, time):
		if time > self.times[-1]:
			i = -2
		else:
			# find interval
			i = 0
			while time > self.times[i]:
				i += 1
			i -= 1

		print(f"i: {i}, time: {time}")
		v1 = self.values[i]
		v2 = self.values[i + 1]
		
		return self.interpolate(time, self.times[i], self.times[i+1], v1, v2)

	@staticmethod
	def interpolate(time, time1, time2, value1, value2):
		"""Given value1 at time1 and value2 at time2 interpolate for time."""
		return None

class LinearInterpolation(Interpolation):
	"""
	Linear interpolation
	"""
	@staticmethod
	def interpolate(time, time1, time2, value1, value2):
		c = time2 - time1
		return (time2 - time) / c * value1 + value2 * (time - time1) / c 

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
	
def resolve_interpolation(s, times, values):
	if s == 'linear':
		return LinearInterpolation(times, values)
	elif s == 'loglinear':
		return LogLinearInterpolation(times, values)
	else:
		raise ValueError(f"Unknown interpolation {s}.")