from dataclasses import dataclass

from straws.curve.basis import Basis, resolve_basis
from straws.curve.discount_curve import DiscountCurve
from straws.instrument.instrument import Instrument
from straws.model.model import Model
from straws.settings import Settings


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
        today = Settings.get_active_settings().today
        self.basis : Basis = resolve_basis(self.basis_type_fixed, today)

    def price_internal(self, on_date):
        time = self.basis.get_time(on_date)
        model = Model.load(self.model_id)
        return model.price_option(self, self.strike, self.maturity, self.flavour, time)
        
    def payoff(self, value, on_date):
        curve:DiscountCurve = DiscountCurve.load(self.discount_curve_id)
        discount = curve.evaluate_on_date(self.maturity) / curve.evaluate_on_date(on_date)
        
        res = (value - self.strike) * self.notional * discount
        if self.flavour == 'put':
            res = -res
        if res < 0:
            res = 0
        return res