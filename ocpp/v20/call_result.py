from typing import Dict, List
from dataclasses import dataclass, field

# Most types of CALLRESULT messages can originate from only 1 source, either
# from a Charge Point or Central System, but not from both.
#
# Take for example the CALLRESULT for an Authorize action. This type of
# CALLRESULT can only be send from a Central System to Charging Station, not
# the other way around.
#
# For some types of CALLRESULT messages the opposite is true; for example for
# the CALLRESULT message for a Reset action. This can only come from a Charge
# Point to a Central System.
#
# The only CALLRESULT that can originate from both a Central System and a
# Charge Point is the CALLRESULT message for a DataTransfer.

# The now following section of classes are for CALLRESULT messages that flow
# from Central System to Charge Point.


@dataclass
class AuthorizePayload:
    certificate_status: str = None
    evse_id: int = None
    id_token_info: Dict = field(default_factory=dict)


@dataclass
class BootNotificationPayload:
    current_time: str
    interval: int
    status: str


@dataclass
class DiagnosticStatusNotificationPayload:
    pass


@dataclass
class FirmwareStatusNotificationPayload:
    pass


@dataclass
class HeartbeatPayload:
    current_time: str


@dataclass
class MeterValuesPayload:
    pass


@dataclass
class StartTransactionPayload:
    transaction_id: int
    id_tag_info: Dict


@dataclass
class StatusNotificationPayload:
    pass


@dataclass
class StopTransactionPayload:
    id_tag_info: Dict = None


@dataclass
class NotifyEventPayload:
    pass


@dataclass
class TransactionEventPayload:
    total_cost: float = None
    charging_priority: int = None
    id_token_info: Dict = None
    updated_personal_message: Dict = None


@dataclass
class NotifyChargingLimitPayload:
    pass


@dataclass
class ClearedChargingLimitPayload:
    pass


@dataclass
class NotifyEVChargingNeedsPayload:
    status: str


@dataclass
class NotifyEVChargingSchedulePayload:
    status: str


@dataclass
class LogStatusNotificationPayload:
    status: str


@dataclass
class NotifyReportPayload:
    pass


@dataclass
class ReservationStatusUpdatePayload:
    pass


@dataclass
class GetCertificateStatusPayload:
    status: str
    ocsp_result: str = None


@dataclass
class Get15118EVCertificate:
    status: str
    exit_response: str
    contract_signature_certificate_chain: Dict = field(default_factory=dict)
    sa_provisioning_certificate_chain: Dict = field(default_factory=dict)


@dataclass
class Update15118EVCertificate:
    status: str
    exit_response: str = None


@dataclass
class GetCertificateStatusRequest:
    status: str
    ocsp_result: str = None

#######################
#######################
#######################
# The CALLRESULT messages that flow from Charge Point to Central System are
# listed in the bottom part of this module.

@dataclass
class CancelReservationPayload:
    status: str


@dataclass
class ChangeAvailabilityPayload:
    status: str


@dataclass
class ChangeConfigurationPayload:
    status: str


@dataclass
class ClearCachePayload:
    status: str


@dataclass
class ClearChargingProfilePayload:
    status: str


@dataclass
class GetCompositeSchedulePayload:
    status: str
    evse_id: int
    schedule: Dict = None


@dataclass
class GetConfigurationPayload:
    configuration_key: Dict = None
    unknown_key: str = None


@dataclass
class GetDiagnosticsPayload:
    file_name: str = None


@dataclass
class GetLocalListVersionPayload:
    version_number: int


@dataclass
class RemoteStartTransactionPayload:
    status: str


@dataclass
class RemoteStopTransactionPayload:
    status: str


@dataclass
class ReserveNowPayload:
    status: str


@dataclass
class ResetPayload:
    status: str


@dataclass
class SendLocalListPayload:
    status: str


@dataclass
class SetChargingProfilePayload:
    status: str


@dataclass
class TriggerMessagePayload:
    status: str


@dataclass
class UnlockConnectorPayload:
    status: str


@dataclass
class UpdateFirmwarePayload:
    pass


@dataclass
class SetVariablesPayload:
    set_variable_result: List = field(default_factory=list)


@dataclass
class GetVariablesPayload:
    get_variable_result: List


@dataclass
class SetNetworkProfilePayload:
    status: str


@dataclass
class GetTransactionStatusPayload:
    ongoing_indicator: bool = None
    messages_in_queue: bool


@dataclass
class RequestStartTransactionPayload:
    status: str
    transaction_id: str = None


@dataclass
class RequestStopTransactionPayload:
    status: str


@dataclass
class CostUpdatedPayload:
    pass


@dataclass
class NotifyCentralChargingNeedsPayload:
    status: str


@dataclass
class Renegotiate15118SchedulePayload:
    status: str


@dataclass
class UpdateFirmwareRequestPayload:
    status: str


@dataclass
class GetLogPayload:
    status: str
    filename: str = None


@dataclass
class SetDisplayMessagePayload:
    status: str


@dataclass
class GetBaseReportPayload:
    status: str


@dataclass
class GetReportPayload:
    status: str


@dataclass
class GetChargingProfilesPayload:
    status: str


@dataclass
class GetInstalledCertificateIds:
    status: str
    certificate_hash_data: Dict = None


@dataclass
class DeleteCertificate:
    status: str


@dataclass
class InstallCertificate:
   status: str


@dataclass
class GetMonitoringReport:
    status: str

# The DataTransfer CALLRESULT can be send both from Central System as well as
# from a Charge Point.


@dataclass
class DataTransferPayload:
    status: str
    data: Dict = None
