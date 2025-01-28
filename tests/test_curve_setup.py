import attr
from matplotlib import pyplot as plt
import pandas as pd
import numpy as np
from typing import * 

from scipy.optimize import root

from straws.curve.linear_curve import LinearCurve


timetable = np.linspace(0.1, 8, 20)

def trade1(curves):
    v = -0.2931530452338909
    times = timetable[:10:2]
    return np.sum(2 * curves[0].values(times)**2 -  curves[1].values(times)**3) - v

def trade2(curves):
    v = -359.1314035087719
    times = timetable[::2]
    return np.sum(100*curves[0].values(times) - 101 * curves[1].values(times)) - v

# def trade3(curves):
#     # v = 
#     times = timetable[5::2]
#     return np.sum(100*curves[0].values(times) - 101 * curves[1].values(times)) - v

def test_curve_setup_2():
    values_curve1 = [1, 0.4, 0.39, 0.29]
    times_curve1 =  [0, 1, 2, 8]
    curve1 = LinearCurve(times=times_curve1, data=values_curve1)
    
    values_curve2 = [1, 0.9, 0.8, 0.7, 0.6]
    times_curve2 =  [0, 1.5, 2, 5, 8]
    curve2 = LinearCurve(times=times_curve2, data=values_curve2)

    print("trade1", trade1([curve1, curve2]))
    print("trade2", trade2([curve1, curve2]))

    curve1.plot()
    curve2.plot()
    plt.show()

def test_curve_setup_1():
    times = [0, timetable[9], timetable[-1]]
    values = [0.9**i for i in range(len(times))]

    curves = [LinearCurve(times=times[:], data=values[:]),
                LinearCurve(times=times[:], data=values[:])]

    trades = [trade1, trade2]

    time_places = [1, 2]

    N = 100
    i = 0
    while i < N: 
        i += 1
        for curve in curves:
            for j in range(len(trades)):
                def func(x):
                    curve.data[time_places[j]] = x[0]
                    return trades[j](curves)
                z = root(func, 0.5).x
                print(curve.data)
        curves[0].plot()
        curves[1].plot()
        plt.show()