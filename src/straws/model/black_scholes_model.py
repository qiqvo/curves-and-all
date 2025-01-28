import numpy as np

from straws.model.model import Model


class BlackScholesModel(Model):
    def __init__(self, name, x0, sigma, mu):
        super().__init__(name, 1, x0)
        self.sigma = sigma
        self.mu = mu

    model_name = 'black_scholes_model'

    def mean(self, t, x):
        return self.mu * x
    
    def variance(self, t, x):
        return self.sigma**2 * np.ones_like(x)
    