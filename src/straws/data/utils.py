from straws.curve.basis import Basis, resolve_basis
from straws.curve.discount_curve import DiscountCurve
from straws.settings import Settings


def get_basis(basis_type) -> Basis:
    today = Settings.get_active_settings().today
    return resolve_basis(basis_type, today)

def get_discount_curve(discount_curve_id) -> DiscountCurve:
    return DiscountCurve.load(discount_curve_id)
