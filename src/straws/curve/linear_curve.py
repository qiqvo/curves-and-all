import attr
from typing import * 
import pandas as pd
import numpy as np

from straws.curve.curve import Curve
from straws.curve.interpolation import LinearInterpolation

@attr.s(slots=True, auto_attribs=True)
class LinearCurve(Curve):
	"""
	Curve with Log linear interpolation.
	"""
	def __attrs_post_init__(self):
		self.interpolation = LinearInterpolation(data=self.data, times=self.times)
