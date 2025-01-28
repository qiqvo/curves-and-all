from matplotlib import pyplot as plt
import numpy as np

from straws.model.hull_white_model import HullWhiteModel
from straws.simulation.simulation import Simulation


def test_hull_white_simulation():
    times = np.linspace(0, 10)
    N = 10

    x0 = [1]
    sigma = 0.2
    mu = 0.0001
    alpha = 0.01

    name = '12'

    model = HullWhiteModel(name, x0, sigma, mu, alpha)
    sim = Simulation(model, N, times)

    paths = sim.simulate()
    # print(paths)
    for i in range(N):
        plt.plot(times, paths[i])
    plt.show()
    
    assert paths.shape == (N, len(times), model.dimension)
    # assert False