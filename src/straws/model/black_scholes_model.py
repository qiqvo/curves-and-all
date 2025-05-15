import numpy as np
from scipy.stats import norm

from straws.model.model import Model


class BlackScholesModel(Model):
    def __init__(self, x0, sigma, mu):
        super().__init__(1, x0)
        self.sigma = sigma
        self.mu = mu

    def drift(self, t, x):
        return self.mu * x
    
    def volatility(self, t, x):
        return self.sigma * x
    
    def price_option(self, strike, maturity, flavour, time):
        # Black-Scholes formula for a European call option
        S = self.x0[0]
        K = strike
        T = maturity - time
        r = self.mu
        sigma = self.sigma

        d1 = (np.log(S / K) + (r + 0.5 * sigma ** 2) * T) / (sigma * np.sqrt(T))
        d2 = d1 - sigma * np.sqrt(T)
        call_price = S * norm.cdf(d1) - K * np.exp(-r * T) * norm.cdf(d2)
        put_price = call_price - S + K * np.exp(-r * T)
        if flavour == 'call':
            return call_price
        elif flavour == 'put':
            return put_price
        else:
            raise ValueError("Invalid option type. Use 'call' or 'put'.")