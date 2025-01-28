import attr
from typing import * 
import pandas as pd
import numpy as np

from curve.curve import Curve
from curve.interpolation import LogLinearInterpolation

@attr.s(slots=True, auto_attribs=True)
class LogLinearCurve(Curve):
	"""
	Curve with Log linear interpolation.
	"""
	def __attrs_post_init__(self):
		self.interpolation = LogLinearInterpolation(data=self.data, times=self.times)