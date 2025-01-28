from abc import abstractmethod
import pandas as pd
import numpy as np


class Model():
    def __init__(self, dimension, x0): 
        self.dimension = dimension
        self.x0 = x0

    @abstractmethod
    def mean(self, t, x):
        pass

    @abstractmethod
    def variance(self, t, x):
        pass