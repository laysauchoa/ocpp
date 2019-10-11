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
class CostUpdatedPayload:
    total_cost: float
    transaction_id: int


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
    charging_profile: Dict = None


@dataclass
class DeleteCertificatePayload:
    certificate_hash_data: Dict = field(default_factory=dict)



@dataclass
class GetChargingProfilesPayload:
    request_id: int = None
    evse_id: int = None
    charging_profile: Dict = field(default_factory=dict)


@dataclass
class GetCompositeSchedulePayload:
    evse_id: int
    duration: int
    charging_rate_unit: str = None


@dataclass
class GetMonitoringReportPayload:
    request_id: int = None
    monitoring_criteria: str = None
    component_variable: Dict = field(default_factory=dict)


@dataclass
class GetReportPayload:
    request_id: int = None
    component_criteria: str = None
    component_variable: Dict = None


@dataclass
class InstallCertificatePayload:
    certificate_type: str
    certificate: str


@dataclass
class NotifyCentralChargingNeedsPayload:
    evse_id: int
    sa_schedule: Dict = field(default_factory=dict)


@dataclass
class Renegotiate15118SchedulePayload:
    evse: Dict = field(default_factory=dict)


@dataclass
class SetNetworkProfilePayload:
    configuration_slot: int
    connection_data: Dict


@dataclass
class GetBaseReportPayload:
    request_id: int
    report_base: str


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
class GetInstalledCertificateIdsPayload:
    type_of_certificate: str


@dataclass
class GetTransactionStatusPayload:
    transaction_id: str = None



@dataclass
class NotifyChargingLimitPayload:
    evse_id: int = None
    charging_limit: Dict = field(default_factory=dict)
    charging_schedule: Dict


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
    group_id_token: Dict = None
    reservation: Dict = field(default_factory=dict)


@dataclass
class ResetPayload:
    type: str


@dataclass
class SendLocalListPayload:
    version_number: int
    update_type: str
    local_authorization_list: List = None


@dataclass
class SetChargingProfilePayload:
    evse_id: int
    charging_profile: Dict = field(default_factory=dict)


@dataclass
class SetDisplayMessagePayload:
    message: Dict = field(default_factory=dict)


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
    retries: int = None
    retry_interval: int = None
    request_id: int
    firmware: Dict = field(default_factory=dict)


# The CALL messages that flow from Charge Point to Central System are listed
# in the bottom part of this module.

@dataclass
class AuthorizePayload:
    evse_id: int = None
    id_token: Dict = field(default_factory=dict)
    _15118_certificate_hash_data: Dict


@dataclass
class BootNotificationPayload:
    reason: str
    charging_station: Dict


@dataclass
class ClearedChargingLimitPayload:
    charging_limit_source: str
    evse_id: int = None


@dataclass
class DiagnosticStatusNotificationPayload:
    status: str


@dataclass
class GetCertificateStatusPayload:
    ocsp_request_data: Dict = field(default_factory=dict)


@dataclass
class Get15118EVCertificate:
    _15118_schema_version: str
    exit_request: str


@dataclass
class LogStatusNotificationPayload:
    status: str
    request_id: int


@dataclass
class NotifyEventPayload:
    generated_at: str
    tbc: bool
    seq_no: int
    event_data: List = field(default_factory=list)
    operational_status: str


@dataclass
class NotifyEVChargingNeedsPayload:
    max_schedule_tuples: int = None
    evse_id: int
    charging_needs: Dict = field(default_factory=dict)


@dataclass
class NotifyEVChargingSchedulePayload:
    time_base: str
    evse_id: int
    charging_schedule: Dict = field(default_factory=dict)


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
class ReservationStatusUpdatePayload:
    reservation_id: int
    reservation_update_status: str


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


@dataclass
class Update15118EVCertificate:
    _15118_schema_version: str
    exit_request: str


# The DataTransfer CALL can be send both from Central System as well as from a
# Charge Point.


@dataclass
class DataTransferPayload:
    vendor_id: str
    message_id: str = None
    data: Any = None
