import numpy as np

from straws.model.model import Model


class HullWhiteModel(Model):
    def __init__(self, name, x0, sigma, mu, alpha):
        super().__init__(name, 1, x0)
        self.sigma = sigma
        self.mu = mu
        self.alpha = alpha

    model_name = 'hull_white_model'

    def drift(self, t, x):
        return self.alpha * (self.mu - x)
    
    def volatility(self, t, x):
        return self.sigma * np.ones_like(x)