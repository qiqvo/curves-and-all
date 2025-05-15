from matplotlib import pyplot as plt
import numpy as np

from straws.model.correlation_provider import CorrelationProvider
from straws.model.hull_white_model import HullWhiteModel
from straws.model.black_scholes_model import BlackScholesModel
from straws.model.combined_model import CombinedModel
from straws.simulation.simulation import Simulation


def test_combined_simulation():
    times = np.linspace(0, 10)
    N = 10

    sigma = 0.2
    mu = 0.0001
    alpha = 0.01
    name = '12'

    model1 = HullWhiteModel(name, 0, sigma, mu, alpha)
    model2 = BlackScholesModel(name, 1, sigma, mu)
    cp = CorrelationProvider({(model1.id, model2.id): 0.5})

    model = CombinedModel(name, [model1, model2], correlation_provider=cp)

    sim = Simulation(model, N, times)

    paths = sim.simulate()
    # print(paths)
    for i in range(2):
        plt.plot(times, paths[i, :, 0])
        plt.plot(times, paths[i, :, 1])
    plt.show()
    
    assert paths.shape == (N, len(times), model.dimension)
    # assert False
