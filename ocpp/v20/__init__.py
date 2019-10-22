from functools import partial
from ocpp.charge_point import ChargePoint as _ChargePoint

ChargePoint = partial(_ChargePoint, ocpp_version="2.0")
