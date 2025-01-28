import numpy as np
from straws.model.model import Model


class CombinedModel(Model):
    def __init__(self, models):
        super().__init__(sum([m.dimension for m in models]), np.concatenate([m.x0 for m in models]))
        self.models = models

    def mean(self, t, x):
        return np.concatenate([m.mean(t, x[i]) for i, m in enumerate(self.models)])
