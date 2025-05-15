from dataclasses import dataclass
import numpy as np

from straws.curve.discount_curve import DiscountCurve


@dataclass
class FlatDiscountCurve(DiscountCurve):
    rate: float 

    def discount(self, time: float) -> float:
        return np.exp(-self.rate * time)
    
    def short_rate(self, time: float) -> float:
        return self.rate