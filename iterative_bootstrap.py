import attr
import typing 
import pandas as pd
import numpy as np

from curve import *
from trade import *

from scipy.optimize import root

@attr.s(slots=True, auto_attribs=True)
class IterativeBootstrap():
    today : pd.Timestamp = attr.ib(default=None)
    trades : list[Trade] = attr.ib(default=None)

    def bootstrap(self, curves : list[Curve], iteration_number=100):
        """
        docstring
        """
        lastest_dates = [trade.lastest_date for trade in self.trades]
        ordered_trades = self.trades[np.argsort(lastest_dates)]

        if len(curves) == 1:
            iteration_number = 1
        
        for iteration in range(iteration_number):
            for curve in curves:
                for trade in ordered_trades:
                    lastest_date = trade.lastest_date
                    def func(x):
                        curve.data.at[lastest_date, "Value"] = x
                        return (trade.price(curves) - trade.value)**2
                    z = root(func, 0)
        
        return curves
