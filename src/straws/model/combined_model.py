import numpy as np
from straws.model.model import Model


class CombinedModel(Model):
    def __init__(self, name, models, correlation_provider):
        super().__init__(name, sum([m.dimension for m in models]), 
                         np.concatenate([m.x0 for m in models]), 
                         correlation_provider)
        a = np.cumsum([0] + [m.dimension for m in models])
        self.dimension_split = [slice(a[i], a[i + 1]) for i in range(len(a) - 1)]
        self.models = models

    model_name = 'combined_model'

    def mean(self, t, x):
        return np.concatenate([m.mean(t, x[:, self.dimension_split[i]]) for i, m in enumerate(self.models)], axis=1)

    def variance(self, t, x):
        return np.concatenate([m.variance(t, x[:, self.dimension_split[i]]) for i, m in enumerate(self.models)], axis=1)
    
    def apply_correlations(self, dW):
        corr = self.correlation_provider.get_corr_matrix([m.name for m in self.models])
        L = np.linalg.cholesky(corr)
        return np.einsum('ijk,kl->ijl', dW, L)