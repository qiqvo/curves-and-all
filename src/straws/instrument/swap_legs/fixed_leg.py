from straws.instrument.swap_legs.base_leg import BaseLeg


class FixedLeg(BaseLeg):
    fixed_rate: float

    def price_internal(self, on_date):
        res = 0
        
        prev_d = on_date
        for d in self.swap_dates:
            if d < on_date:
                continue
            else:
                res += self.fixed_rate \
                    * self.basis.get_delta(prev_d, d) \
                    * self.discount_curve.discount_on_date(on_date, d)
            prev_d = d
        return res