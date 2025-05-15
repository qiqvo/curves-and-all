from abc import abstractmethod
import numpy as np

from straws.data.pure_object_data import PureObjectData
from straws.model.correlation_provider import CorrelationProvider


class Model(PureObjectData):
    def __init__(self, dimension: int, x0, correlation_provider: CorrelationProvider=None): 
        self.dimension = dimension
        self.x0 = np.zeros(dimension)
        self.x0[:dimension] = x0
        self.correlation_provider = correlation_provider

    @abstractmethod
    def drift(self, t, x):
        pass

    @abstractmethod
    def volatility(self, t, x):
        pass
    
    def apply_correlations(self, dW):
        return dW
    
    def price_option(self, strike, maturity, flavour, time):
        raise NotImplementedError("Price method not implemented for this model")