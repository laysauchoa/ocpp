from typing import Any, Dict, List
from dataclasses import dataclass, field

# Most types of CALL messages can originate from only 1 source, either
# from a Charge Point or Central System, but not from both.
#
# Take for example the CALL for an ChangeConfiguration action. This type of
# CALL can only be send from a Central System to Charging Station, not
# the other way around.
#
# For some types of CALL messages the opposite is true; for example for the
# CALL message for a BootNotification action. This can only come from a Charge
# Point and send to a Central System.
#
# The only CALL that can originate from both a Central System and a
# Charge Point is the CALL message for a DataTransfer.

# The now following section of classes are for CALL messages that flow
# from Central System to Charge Point.


@dataclass
class CancelReservationPayload:
    reservation_id: int


@dataclass
class ChangeAvailabilityPayload:
    evse_id: int
    operational_status: str


@dataclass
class SetVariablesPayload:
    # TODO: Should we create a SetVariableDataType Dict and pass it here?
    set_variable_data: Dict = field(default_factory=dict)


@dataclass
class ClearCachePayload:
    pass


@dataclass
class ClearChargingProfilePayload:
    evse_id: int = None
    charging_profile: Dict = field(default_factory=dict)
    stack_level: int = None


@dataclass
class GetCompositeSchedulePayload:
    evse_id: int
    duration: int
    charging_rate_unit: str = None


@dataclass
class GetVariablesPayload:
    get_variable_data: Dict = field(default_factory=dict)


@dataclass
class GetLogPayload:
    log_type: str
    request_id: int
    retries: int = None
    retry_interval: int = None
    log: Dict = field(default_factory=dict)


@dataclass
class GetLocalListVersionPayload:
    pass


@dataclass
class RequestStartTransactionPayload:
    evse_id: int = None
    remote_start_id: int
    id_token: Dict = field(default_factory=dict)
    charging_profile: Dict = None


@dataclass
class RequestStopTransactionPayload:
    transaction_id: int


@dataclass
class ReserveNowPayload:
    id_token: Dict = field(default_factory=dict)
    group_id_token: Dict
    reservation: Dict = field(default_factory=dict)


@dataclass
class ResetPayload:
    type: str


@dataclass
class SendLocalListPayload:
    version_number: int
    update_type: str
    local_authorization_list: List = field(default_factory=list)


@dataclass
class SetChargingProfilePayload:
    evse_id: int
    charging_profile: Dict


@dataclass
class TriggerMessagePayload:
    requested_message: str
    evse: Dict = None


@dataclass
class UnlockConnectorPayload:
    evse_id: int
    connector_id: int


@dataclass
class UpdateFirmwarePayload:
    firmware: Dict
    request_id: int
    retrieve_date: str
    retries: int = None
    retry_interval: int = None


# The CALL messages that flow from Charge Point to Central System are listed
# in the bottom part of this module.

@dataclass
class AuthorizePayload:
    evse_id: int = None
    id_token: Dict = field(default_factory=dict)
    id_tag: str


@dataclass
class BootNotificationPayload:
    reason: str
    charging_station: Dict


@dataclass
class LogStatusNotificationPayload:
    status: str
    request_id: int


@dataclass
class PublishFirmwareStatusNotificationPayload:
    status: str
    location: str = None


@dataclass
class HeartbeatPayload:
    pass


@dataclass
class MeterValuesPayload:
    """
    Depricated
    """
    evse_id: int
    meter_value: Dict = field(default_factory=dict)


@dataclass
class StatusNotificationPayload:
    timestamp: str = None
    connector_status: str
    evse_id: int
    connector_id: int


@dataclass
class TransactionEventPayload:
    event_type: str
    timestamp: str = None
    trigger_reason: str
    seq_no: int
    offline: bool = None
    number_of_phases_used: int = None
    cable_max_current: float = None
    reservation_id: int = None
    transaction_data: Dict = field(default_factory=dict)
    id_token: Dict = None
    evse: Dict = None
    meter_value: Dict = None

# The DataTransfer CALL can be send both from Central System as well as from a
# Charge Point.


@dataclass
class DataTransferPayload:
    vendor_id: str
    message_id: str = None
    data: Any = None
