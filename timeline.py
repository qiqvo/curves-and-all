import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import math
import attr
import os
from interpolation import BasisAct365

@attr.s(slots=True, auto_attribs=True)
class Timeline:
    """
    Implements timeline.
    """
    as_of_date: str = attr.ib(default=None, kw_only=True)
    """AsOfDate."""

    simulation_times: pd.Series = attr.ib(default=None, kw_only=True)
    """Times, index is date."""

    basis: BasisAct365 = attr.ib(default=None, kw_only=True)
    """Basis"""

    def Create(self, dates):
        self.as_of_date = dates[0]
        self.basis = BasisAct365(self.as_of_date)
        self.simulation_times = pd.Series(data=[self.basis.get_time(date) for date in dates], index=dates)
        self.simulation_times = self.simulation_times.sort_values(axis=0)

    def get_time(self, date):
        time = self.basis.get_time(date)
        return time

    def get_next_date_time(self, curr_date):
        for date in self.simulation_times.index:
            if date >= curr_date:
                return date, self.simulation_times[date]

    def get_prev_date_time(self, curr_date):
        for date in self.simulation_times.index[::-1]:
            if date <= curr_date:
                return date, self.simulation_times[date]