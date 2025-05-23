from dataclasses import dataclass

from straws.data.utils import get_basis, get_discount_curve
from straws.instrument.instrument import Instrument
from straws.model.model import Model


@dataclass
class Option(Instrument):
    flavour: str 
    notional: float 
    currency: str 
    model_id: str  
    strike: float  
    discount_curve_id: str  
    basis_type: str 

    def __post_init__(self):
        self.discount_curve = get_discount_curve(self.discount_curve_id)
        self.basis = get_basis(self.basis_type)

    def price_internal(self, on_date):
        time = self.basis.get_time(on_date)
        model = Model.load(self.model_id)
        return model.price_option(self, self.strike, self.maturity, self.flavour, time)
        
    def payoff(self, value, on_date):
        discount = self.discount_curve.discount_on_date(on_date, self.maturity)
        
        res = (value - self.strike) * self.notional * discount
        if self.flavour == 'put':
            res = -res
        if res < 0:
            res = 0
        return res