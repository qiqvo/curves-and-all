from dataclasses import dataclass
from typing import * 
import numpy as np

from straws.curve.curve import Curve

@dataclass
class DiscountCurve(Curve):
    def discount(self, time: float) -> float:
        return self.evaluate(time)
    
    def short_rate(self,  time: float) -> float:
        # Calculate the short rate from the discount factor
        return -np.log(self.discount(time)) / time
    
    def discount_on_date(self, on_date, date=None):
        if date is None:
            return self.evaluate_on_date(on_date)
        else:
            return self.evaluate_on_date(date) / self.evaluate_on_date(on_date)