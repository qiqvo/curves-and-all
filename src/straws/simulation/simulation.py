from typing import List
import numpy as np

from straws.model.model import Model


class Simulation():
    def __init__(self, model: Model, N, times: List[float]): 
        self.model = model
        self.x0 = model.x0
        self.dimension = model.dimension

        self.N = N
        self.times = times
        # self.simulated = False

    def simulate(self):
        dt = np.diff(self.times)
        n = len(self.times)
        paths = np.zeros((self.N, n, self.dimension))

        paths[:, 0] = self.x0

        for i in range(1, n):
            dW = np.random.normal(size=(self.N, n-1, self.dimension))
            
            paths[:, i, :] = paths[:, i-1, :]
            paths[:, i, :] += self.model.mean(self.times[i-1], paths[:, i-1, :]) * dt[i-1] 
            paths[:, i, :] += self.model.variance(self.times[i-1], paths[:, i-1, :]) * np.sqrt(dt[i-1]) * dW[:, i-1, :] 
            #paths[:, i-1] * np.exp((self.mu - 0.5 * self.sigma ** 2) * dt[i-1] + self.sigma * np.sqrt(dt[i-1]) * dW[:, i-1])

        # self.simulated = True
        return paths
    