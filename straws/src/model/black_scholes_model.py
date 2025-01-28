import numpy as np

from model.model import Model


class BlackScholesModel(Model):
    def __init__(self, x0, sigma, mu):
        super().__init__(1, x0)
        self.sigma = sigma
        self.mu = mu

    def mean(self, t, x):
        return self.mu * x
    
    def variance(self, t, x):
        return self.sigma**2
    