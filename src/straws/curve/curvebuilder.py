from dataclasses import dataclass
from typing import * 
import numpy as np
from scipy.optimize import brentq


from straws.curve.basis import Basis, resolve_basis
from straws.curve.interpolated_curve import InterpolatedCurve
from straws.data.opaque_object_data import OpaqueObjectData
from straws.instrument.instrument import Instrument
from straws.settings import Settings

@dataclass
class Curvebuilder(OpaqueObjectData):
	instruments: List[Instrument] 
	curve_id: List[str]
	interpolation_type: str 
	basis_type : str

	def build(self):
		today = Settings.get_active_settings().today
		# basis : Basis = resolve_basis(self.basis_type, today)

		instruments = sorted(self.instruments, key=lambda x: x.maturity)
		dates = [today]
		values = [1.0]
		curve = InterpolatedCurve(self.basis_type, 
							dates, values, 
							self.interpolation_type,
							id=self.curve_id)

		for instrument in instruments:
			dates.append(instrument.maturity)
			values.append(values[-1])
			
			def J(x):
				curve.values[-1] = x
				# TODO: explore how to create a temporary registry and save in it
				curve.save()
				return instrument.price()

			values[-1] = brentq(J, 1e-10, 1.4, maxiter=1000)

		curve = InterpolatedCurve(self.basis_type, 
							dates, values, 
							self.interpolation_type,
							id=self.curve_id)
		return curve