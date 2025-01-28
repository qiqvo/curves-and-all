from abc import abstractmethod
import pandas as pd
import numpy as np

from straws.model.correlation_provider import CorrelationProvider


class Model():
    def __init__(self, name: str, dimension: int, x0, correlation_provider: CorrelationProvider=None): 
        self.name_id = name
        self.dimension = dimension
        self.x0 = np.zeros(dimension)
        self.x0[:dimension] = x0
        
        self.correlation_provider = correlation_provider

    model_name = 'base_model'

    @property
    def name(self):
        return self.model_name + ':' + self.name_id    

    @abstractmethod
    def mean(self, t, x):
        pass

    @abstractmethod
    def variance(self, t, x):
        pass
    
    def apply_correlations(self, dW):
        return dW