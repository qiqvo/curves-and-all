import attr
import typing 
import pandas as pd
import numpy as np

from curve import *
from trade import *
from iterative_bootstrap import *

timetable = np.linspace(0.1, 20, 30)

def trade1(curves):
    times = timetable[::2]
    return [curves[0].value(time) for time in times]

def main():
    basis, curve = create_basis_curve()
    today = basis.today

    trade1 = LiborTrade(basis=basis, quote=0.035, \
                quantity=1, cashflow_dates=[today + pd.Timedelta(days=100)])
    trade2 = FuturesTrade(basis=basis, quote=0.03, \
                quantity=1, \
                cashflow_dates=[today + pd.Timedelta(days=100), today + pd.Timedelta(days=200)])
    
    

if __name__ == "__main__":
    main()