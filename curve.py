import attr
import typing 
import pandas as pd
import numpy as np

from basis import *
from interpolation import *
import matplotlib.pyplot as plt

@attr.s(slots=True, auto_attribs=True)
class Curve():
	"""
	Curve has elements:
		basis
		interpolation
		data
	"""
	data : pd.DataFrame = attr.ib(default=None)
	basis : Basis = attr.ib(default=None)
	interpolation : Interpolation = attr.ib(default=None)
	name : str = attr.ib(default=None)

	def __attrs_post_init__(self):
		self.data.set_index("Date")
		dates = self.data.index
		times = [self.basis.get_time(date) for date in dates]
		self.data.insert(0, "Time", times, True)
		self.data.rename(columns={self.name : 'Value'}, inplace=True)
		# self.interpolation = LinearInterpolation(self.data)

	def value(self, date=None, time=None):
		if date is not None:
			time = self.basis.get_time(date)
		return self.interpolation.value(time)

	def plot(self, end_date):
		time0 = self.basis.today
		time1 = self.basis.get_time(end_date)

		times = np.linspace(time0, time1)
		plt.plot(times, self.value(time=times))
		plt.scatter(self.data["Time"], self.data['Value'], c='r')
		# plt.show()

@attr.s(slots=True, auto_attribs=True)
class LinearCurve(Curve):
	"""
	Curve with Log linear interpolation.
	"""
	def __attrs_post_init__(self):
		self.interpolation = LinearInterpolation(self.data)

@attr.s(slots=True, auto_attribs=True)
class LogLinearCurve(Curve):
	"""
	Curve with Log linear interpolation.
	"""
	def __attrs_post_init__(self):
		self.interpolation = LogLinearInterpolation(self.data)


def create_basis_curve():
	data = np.array([["2020-09-18", 1.0], 
						["2020-12-20", 0.998982370689909],
						["2021-06-20", 0.997500050423405],
						["2022-06-20", 0.989998832273272]])
	data = pd.DataFrame(data, columns=['Date', 'Sp'])
	dates = pd.to_datetime(data["Date"].values)

	data.drop(columns=["Date"], inplace=True)
	data.insert(0, "Date", dates, True)
	data['Sp'] = data['Sp'].astype(float)

	basis = BasisAct360(pd.to_datetime("2020-09-18"))
	sp_curve = LogLinearCurve(data, basis, 'Sp')
	
	return basis, sp_curve

def test():
	"""Test."""
	basis, sp_curve = create_basis_curve()
	
	print(pd.to_datetime("2020-10-15"), basis.get_time(pd.to_datetime("2020-10-15")), sp_curve.value(pd.to_datetime("2020-10-15")))
	print(pd.to_datetime("2021-01-15"), basis.get_time(pd.to_datetime("2021-01-15")), sp_curve.value(pd.to_datetime("2021-01-15")))
	print(pd.to_datetime("2021-04-15"), basis.get_time(pd.to_datetime("2021-04-15")), sp_curve.value(pd.to_datetime("2021-04-15")))
	print(pd.to_datetime("2022-04-15"), basis.get_time(pd.to_datetime("2022-04-15")), sp_curve.value(pd.to_datetime("2022-04-15")))