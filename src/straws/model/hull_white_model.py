import numpy as np

from straws.model.model import Model


class HullWhiteModel(Model):
    def __init__(self, x0, sigma, mu, alpha):
        super().__init__(1, x0)
        self.sigma = sigma
        self.mu = mu
        self.alpha = alpha

    def mean(self, t, x):
        return self.alpha * (self.mu - x)
    
    def variance(self, t, x):
        return self.sigma**2