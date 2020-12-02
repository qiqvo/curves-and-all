import attr
import typing
from numpy.lib.function_base import quantile 
import pandas as pd
import numpy as np
from pandas.tseries import frequencies

from curve import *

@attr.s(slots=True, auto_attribs=True)
class Cashflow():
	date : pd.Timestamp = attr.ib(default=None)
	quantity : float = attr.ib(default=None)

	@staticmethod
	def price(self, curves=None):
		return self.quantity * curves[0].value(self.date)

@attr.s(slots=True, auto_attribs=True)
class Trade():
	"""
	cashflows
	quote	
	"""
	basis : Basis = attr.ib(default=0)
	quote : float = attr.ib(default=None)
	quantity : float = attr.ib(default=None)

	cashflow_dates : list[pd.Timestamp] = attr.ib(default=None)

	lastest_date : pd.Timestamp = attr.ib(default=None)
	cashflows : list[Cashflow] = attr.ib(default=None)

	def __attrs_post_init__(self):
		self.lastest_date = pd.max(self.cashflow_dates)

	def price(self, curves=None):
		return np.sum([cashflow.price(curves) for cashflow in self.cashflows])


@attr.s(slots=True, auto_attribs=True)
class FuturesTrade(Trade):
	def check_number_of_cashflows(self):
		if len(self.cashflow_dates) > 2:
			raise "more dates than needed"
		if len(self.cashflow_dates) < 2:
			raise "less dates than needed"
		
	def prepare(self):
		pass

	def __attrs_post_init__(self):
		self.check_number_of_cashflows()
		self.prepare()
		
		delta0 = self.basis.get_time(self.cashflow_dates[0])
		delta1 = self.basis.get_time(self.cashflow_dates[1])
		
		cashflow0 = Cashflow(date=self.cashflow_dates[0], \
					quantity=-self.quantity)
		cashflow1 = Cashflow(date=self.cashflow_dates[1], \
					quantity=+self.quantity * (1 + self.quote * (delta1 - delta0)))

		self.cashflows = [cashflow0, cashflow1]
		self.lastest_date = self.cashflow_dates[1]


@attr.s(slots=True, auto_attribs=True)
class LiborTrade(FuturesTrade):
	def check_number_of_cashflows(self):
		if len(self.cashflow_dates) > 1:
			raise "more dates than needed"
		if len(self.cashflow_dates) < 1:
			raise "less dates than needed"

	def prepare(self):
		self.cashflow_dates.insert(0, self.basis.today)


@attr.s(slots=True, auto_attribs=True)
class SwapTrade(Trade):
	buy_date : pd.Timestamp = attr.ib(default=None)
	start_date : pd.Timestamp = attr.ib(default=None)
	end_date : pd.Timestamp = attr.ib(default=None)
	frequency : pd.Timedelta = attr.ib(default=None)

	def prepare_cashflow_dates(self):
		self.cashflow_dates = [self.buy_date]
		cashflow_date = self.start_date
		while cashflow_date < self.end_date:
			self.cashflow_dates.append(cashflow_date)
			cashflow_date = cashflow_date + self.frequency
		self.cashflow_dates.append(self.end_date)

	def __attrs_post_init__(self):
		# self.check_number_of_cashflows()
		self.prepare_cashflow_dates()
		deltas = [self.basis.get_time(cashflow_date) for cashflow_date in self.cashflow_dates]
		values = [-1]
		values.append([self.quote * (deltas[i] - deltas[i-1]) for i in range(1, len(deltas))])
		values[-1] += 1

		self.cashflows = [Cashflow(date=self.cashflow_dates[i], \
						quantity=self.quantity * values[i]) for i in range(len(values))]

		self.lastest_date = self.end_date
