from straws.curve.discount_curve import DiscountCurve
from straws.instrument.swap_legs.base_leg import BaseLeg


class FloatLeg(BaseLeg):
    floating_curve_id: str

    def __post_init__(self):
        super().__post_init__()
        self.floating_curve: DiscountCurve = self.get_discount_curve(self.floating_curve_id)

    def price_internal(self, on_date):
        res = 0
        prev_d = on_date
        for d in self.swap_dates:
            if d < on_date:
                continue
            else:
                res += (self.floating_curve.evaluate_on_date(prev_d)/self.floating_curve.evaluate_on_date(d) - 1)
                # L /= self.floating_curve.basis.get_delta(on_date, d)
            prev_d = d
        return res