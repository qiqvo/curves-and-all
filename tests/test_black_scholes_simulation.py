from matplotlib import pyplot as plt
import numpy as np

from straws.model.black_scholes_model import BlackScholesModel
from straws.simulation.simulation import Simulation


def test_black_scholes_simulation():
    times = np.linspace(0, 10)
    N = 10

    x0 = 1
    sigma = 0.2
    mu = 0.1

    model = BlackScholesModel(x0, sigma, mu)
    sim = Simulation(model, N, times)

    paths = sim.simulate()
    # print(paths)
    plt.plot(times, paths[0])
    # assert paths.shape == (N, len(times), model.dimension)
    assert False