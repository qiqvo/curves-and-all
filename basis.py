# Copyright (C) 2003-present CompatibL. All rights reserved.
#
# This file contains valuable trade secrets and may be copied, stored, used,
# or distributed only in compliance with the terms of a written commercial
# license from CompatibL and with the inclusion of this copyright notice.

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import math


class Basis(object):
	"""Abstract basis."""
	def __init__(self, today):
		super(Basis, self).__init__()
		self.today = pd.to_datetime(today)

	@staticmethod
	def get_time(self, date):
		pass

class BasisAct360(Basis):
	"""
	Basis act/360
	"""
	def __init__(self, today):
		super(BasisAct360, self).__init__(today)

	def get_time(self, date):
		date = pd.to_datetime(date)
		if date == self.today:
			return 0
		return (date - self.today) / np.timedelta64(1,'D') / 360


class BasisAct365(Basis):
	"""
	Basis act/365
	"""
	def __init__(self, today):
		super(BasisAct365, self).__init__(today)

	def get_time(self, date):
		date = pd.to_datetime(date)
		if date == self.today:
			return 0
		return (date - self.today) / np.timedelta64(1,'D') / 365