import numpy as np

from straws.model.model import Model


class HullWhiteModel(Model):
    def __init__(self, x0, sigma, mu, alpha):
        super().__init__(1, x0)
        self.sigma = sigma
        self.mu = mu
        self.alpha = alpha

    def drift(self, t, x):
        return self.alpha * (self.mu - x)
    
    def volatility(self, t, x):
        return self.sigma * np.ones_like(x)