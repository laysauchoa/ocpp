class Action:
    """ An Action is a required part of a Call message. """
    Authorize = "Authorize"
    BootNotification = "BootNotification"
    CancelReservation = "CancelReservation"
    ChangeAvailability = "ChangeAvailability"
    ChangeConfiguration = "ChangeConfiguration"
    ClearCache = "ClearCache"
    ClearChargingProfile = "ClearChargingProfile"
    DataTransfer = "DataTransfer"
    DiagnosticStatusNotification = "DiagnosticStatusNotification"
    FirmwareStatusNotification = "FirmwareStatusNotification"
    GetCompositeSchedule = "GetCompositeSchedule"
    GetConfiguration = "GetConfiguration"
    ClearChargingProfile = "ClearChargingProfile"
    GetDiagnostics = "GetDiagnostics"
    GetLocalListVersion = "GetLocalListVersion"
    Heartbeat = "Heartbeat"
    MeterValues = "MeterValues"
    RemoteStartTransaction = "RemoteStartTransaction"
    RemoteStopTransacton = "RemoteStopTransaction"
    ReserveNow = "ReserveNow"
    Reset = "Reset"
    SendLocalList = "SendLocalList"
    SetChargingProfile = "SetChargingProfile"
    StartTransaction = "StartTransaction"
    StatusNotification = "StatusNotification"
    StopTransaction = "StopTransaction"
    TriggerMessage = "TriggerMessage"
    UnlockConnector = "UnlockConnector"
    UpdateFirmware = "UpdateFirmware"


class MessageType:
    Call = 2
    CallResult = 3
    CallError = 4


class NotifyEVChargingNeedsStatusEnumType:
    """
    NotifyEVChargingNeedsStatusEnumType is used by:
    notifyEVChargingNeeds:NotifyEVChargingNeedsResponse

    Accepted: a SASchedule will be provided momentarily.
    Rejected: Service is Not Available
    Processing: The CSMS is gathering information to provide an SASchedule.
    """
    accepted = "Accepted"
    rejected = "Rejected"
    processing = "Processing"


class GenericStatusEnumType:
    """
    Generic message response status
    GenericStatusEnumType is used by:
    notifyCentralChargingNeeds:NotifyCentralChargingNeedsResponse,
    notifyEVChargingSchedule:NotifyEVChargingScheduleResponse,
    renegotiate15118Schedule:Renegotiate15118ScheduleResponse,
    signCertificate:SignCertificateResponse,
    setMonitoringLevel:SetMonitoringLevelResponse,
    publishFirmware:PublishFirmwareResponse,
    getCertificateStatus:GetCertificateStatusResponse
    """
    accepted = "Accepted"
    rejected = "Rejected"


class LogEnumType:
    """
    LogEnumType is used by: getLog:GetLogRequest
    """
    diagnosticsLog = "DiagnosticsLog"
    securityLog = "SecurityLog"


class AttributeEnumType:
    """
    AttributeEnumType is used by: Common:VariableAttributeType,
    getVariables:GetVariablesRequest.GetVariableDataType,
    getVariables:GetVariablesResponse.GetVariableResultType,
    setVariables:SetVariablesRequest.SetVariableDataType,
    setVariables:SetVariablesResponse.SetVariableResultType
    """
    actual = "Actual"
    target = "Target"
    min_set = "MinSet"
    max_set = "MaxSet"


class AuthorizationStatusEnumType:
    """
    Status of an authorization response.
    AuthorizationStatusEnumType is used by: Common:IdTokenInfoType
    "ConcurrentTx": Identifier is already involved in another transaction and
    multiple transactions are not allowed. (Only relevant for the response to a
    transactionEventRequest(eventType=Started).)
    "NoCredit": Identifier is valid, but EV Driver doesn’t have enough credit
    to start charging. Not allowed for charging.
    "NotAllowedTypeEVSE": Identifier is valid, but not allowed to charge in
    this type of EVSE.
    "NotAtThisLocation": Identifier is valid, but not allowed to charge it
    this location.
    "NotAtThisTime": Identifier is valid, but not allowed to charge it this
    location at this time.
    "Unknown": Identifier is unknown. Not allowed for charging.
    """

    accepted = "Accepted"
    blocked = "Blocked"
    expired = "Expired"
    invalid = "Invalid"
    concurrenttx = "ConcurrentTx"
    no_credit = "NoCredit"
    not_allowed_type_evse = "NotAllowedTypeEVSE"
    not_at_this_location = "NotAtThisLocation"


class ChangeAvailabilityStatusEnumType:
    """
    Status returned in response to ChangeAvailabilityRequest.
    "Scheduled": Request has been accepted and will be executed when
    transaction(s) in progress have finished.
    """

    accepted = "Accepted"
    rejected = "Rejected"
    scheduled = "Scheduled"


class OperationalStatusEnumType:
    """
    Requested availability change in ChangeAvailability.req.
    """

    inoperative = "Inoperative"
    operative = "Operative"


class CancelReservationStatusEnumType:
    """
    Status in CancelReservation.conf.
    """

    accepted = "Accepted"
    rejected = "Rejected"


class ChargePointErrorCode:
    """
    Charge Point status reported in StatusNotification.req.
    """

    connectorLockFailure = "ConnectorLockFailure"
    evCommunicationError = "EVCommunicationError"
    groundFailure = "GroundFailure"
    highTemperature = "HighTemperature"
    internalError = "InternalError"
    localListConflict = "LocalListConflict"
    noError = "NoError"
    otherError = "OtherError"
    overCurrentFailure = "OverCurrentFailure"
    overVoltage = "OverVoltage"
    powerMeterFailure = "PowerMeterFailure"
    powerSwitchFailure = "PowerSwitchFailure"
    readerFailure = "ReaderFailure"
    resetFailure = "ResetFailure"
    underVoltage = "UnderVoltage"
    weakSignal = "WeakSignal"


class ConnectorStatusEnumType:
    """
    A status can be reported for the Connector of an EVSE of a
    Charging Station.
    States considered Operative are: Available, Reserved and Occupied.
    States considered Inoperative are: Unavailable, Faulted.
    ConnectorStatusEnumType is used by:
    statusNotification:StatusNotificationRequest
    """

    available = "Available"
    occupied = "Occupied"
    reserved = "Reserved"
    unavailable = "Unavailable"
    faulted = "Faulted"


class ChargingProfileKindEnumType:
    """
    ChargingProfileKindEnumType is used by: Common:ChargingProfileType

    "Absolute": Schedule periods are relative to a fixed point in time defined
                in the schedule.
    "Recurring": Schedule restarts periodically at the first schedule period.
    "Relative": Schedule periods are relative to a situation- specific start
                point(such as the start of a session)
    """

    absolute = "Absolute"
    recurring = "Recurring"
    relative = "Relative"


class ChargingProfilePurposeType:
    """
    ChargingProfilePurposeEnumType is used by: Common:ChargingProfileType ,
    clearChargingProfile:ClearChargingProfileRequest.ClearChargingProfileType,
    getChargingProfiles:GetChargingProfilesRequest.ChargingProfileCriterionType

    In load balancing scenarios, the Charge Point has one or more local
    charging profiles that limit the power or current to be shared by all
    connectors of the Charge Point. The Central System SHALL configure such
    a profile with ChargingProfilePurpose set to “ChargePointMaxProfile”.
    ChargePointMaxProfile can only be set at Charge Point ConnectorId 0.

    Default schedules for new transactions MAY be used to impose charging
    policies. An example could be a policy that prevents charging during
    the day. For schedules of this purpose, ChargingProfilePurpose SHALL
    be set to TxDefaultProfile. If TxDefaultProfile is set to ConnectorId 0,
    the TxDefaultProfile is applicable to all Connectors. If ConnectorId is
    set >0, it only applies to that specific connector. In the event a
    TxDefaultProfile for connector 0 is installed, and the Central
    System sends a new profile with ConnectorId >0, the TxDefaultProfile
    SHALL be replaced only for that specific connector.

    If a transaction-specific profile with purpose TxProfile is present,
    it SHALL overrule the default charging profile with purpose
    TxDefaultProfile for the duration of the current transaction only.
    After the transaction is stopped, the profile SHOULD be deleted.
    If there is no transaction active on the connector specified in a
    charging profile of type TxProfile, then the Charge Point SHALL
    discard it and return an error status in SetChargingProfile.conf.
    TxProfile SHALL only be set at Charge Point ConnectorId >0.

    It is not possible to set a ChargingProfile with purpose set to
    TxProfile without presence of an active transaction, or in advance of
    a transaction.

    In order to ensure that the updated charging profile applies only to the
    current transaction, the chargingProfilePurpose of the ChargingProfile
    MUST be set to TxProfile.

    #TODO: Definitions of every profile kind
    """

    cs_max_profile = "ChargingStationMaxProfile"
    txdefault_profile = "TxDefaultProfile"
    txprofile = "TxProfile"
    cs_external_constraints = "ChargingStationExternalConstraints"


class ChargingProfileStatusEnumType:
    """
    Status returned in response to SetChargingProfile.req
    ChargingProfileStatusEnumType is used by:
    setChargingProfile:SetChargingProfileResponse
    """

    accepted = "Accepted"
    rejected = "Rejected"


class ChargingRateUnitEnumType:
    """
    Unit in which a charging schedule is defined, as used in:
    GetCompositeSchedule.req and ChargingSchedule
    """

    watts = "W"
    amps = "A"


class ChargingStateEnumType:
    """
    Reason that triggered a transactionEventRequest(eventType=Updated) to be
    sent. ChargingStateEnumType is used by:
    transactionEvent:TransactionEventRequest.TransactionType
    """

    charging = "Charging"
    ev_detected = "EVDetected"
    suspended_ev = "SuspendedEV"
    suspended_evse = "SuspendedEVSE"


class ClearCacheStatusEnumType:
    """
    Status returned in response to ClearCache.req.
    """

    accepted = "Accepted"
    rejected = "Rejected"


class ClearChargingProfileStatusEnumType:
    """
    Status returned in response to ClearChargingProfile.req.
    """

    accepted = "Accepted"
    unknown = "Unknown"


class ClearMessageStatusEnumType:
    """
    Result for a ClearDisplayMessageRequest as used in a
    ClearDisplayMessageResponse. ClearMessageStatusEnumType is used by:
    clearDisplayMessage:ClearDisplayMessageResponse
    """

    accepted = "Accepted"
    unknown = "Unknown"


class ClearMonitoringStatusEnumType:
    """
    ClearMonitoringStatusEnumType is used by: Common:ClearMonitoringResultType
    """

    accepted = "Accepted"
    rejected = "Rejected"
    not_found = "NotFound"


class ComponentCriterionEnumType:
    """
    ClearMonitoringStatusEnumType is used by: Common:ClearMonitoringResultType
    """

    active = "Active"
    available = "Available"
    enabled = "Enabled"
    problem = "Problem"


# TODO: ConnectorEnumType


class SetVariableStatusEnumType:
    """
    SetVariableStatusEnumType is used by:
    setVariables:SetVariablesResponse.SetVariableResultType
    """

    accepted = "Accepted"
    rejected = "Rejected"
    invalid = "InvalidValue"
    unknown_component = "UnknownComponent"
    unknown_variable = "UnknownVariable"
    reboot_required = "RebootRequired"
    not_supported_attribute_type = "NotSupportedAttributeType"
    out_of_range = "OutOfRange"


class DataTransferStatusEnumType:
    """
    Status in DataTransfer.conf.
    """
    accepted = "Accepted"
    rejected = "Rejected"
    unknown_message_id = "UnknownMessageId"
    unknown_vendor_id = "UnknownVendorId"


class UploadLogStatusEnumType:
    """
    Status in DiagnosticsStatusNotification.req.
    """

    idle = "Idle"
    uploaded = "Uploaded"
    uploadFailed = "UploadFailed"
    uploading = "Uploading"


class FirmwareStatusEnumType:
    """
    Status of a firmware download.
    A value with "Intermediate state" in the description,
    is an intermediate state, update process is not finished.
    A value with "Failure end state" in the description, is an end state,
    update process has stopped, update failed.
    A value with "Successful end state" in the description, is an end state,
    update process has stopped, update successful.
    FirmwareStatusEnumType is used by:
    FirmwareStatusNotification:FirmwareStatusNotificationRequest
    """
    # TODO: ADD the rest of the properties
    downloaded = "Downloaded"
    downloadFailed = "DownloadFailed"
    downloading = "Downloading"
    idle = "Idle"
    installationFailed = "InstallationFailed"
    installing = "Installing"
    installed = "Installed"


class GetCompositeScheduleStatusEnumType:
    """
    Status returned in response to GetCompositeSchedule.req
    """

    accepted = "Accepted"
    rejected = "Rejected"


class LocationEnumType:
    """
    Allowable values of the optional "location" field of a value element in
    SampledValue.
    """

    inlet = "Inlet"
    outlet = "Outlet"
    body = "Body"
    cable = "Cable"
    ev = "EV"


class MeasurandEnumType:
    """
    Allowable values of the optional "measurand" field of a Value element, as
    used in MeterValues.req and StopTransaction.req messages. Default value of
    "measurand" is always "Energy.Active.Import.Register"
    """

    currentExport = "Current.Export"
    currentImport = "Current.Import"
    currentOffered = "Current.Offered"
    energyActiveExportRegister = "Energy.Active.Export.Register"
    energyActiveImportRegister = "Energy.Active.Import.Register"
    energyReactiveExportRegister = "Energy.Reactive.Export.Register"
    energyReactiveImportRegister = "Energy.Reactive.Import.Register"
    energyActiveExportInterval = "Energy.Active.Export.Interval"
    energyActiveImportInterval = "Energy.Active.Import.Interval"
    energyActiveNet = "Energy.Active.Net"
    energyReactiveExportInterval = "Energy.Reactive.Export.Interval"
    energyReactiveImportInterval = "Energy.Reactive.Import.Interval"
    energyReactiveNet = "Energy.Reactive.Net"
    energyAparentNet = "Energy.Aparent.Net"
    energyAparentImport = "Energy.Aparent.Import"
    energyAparentExport = "Energy.Aparent.Export"
    frequency = "Frequency"
    powerActiveExport = "Power.Active.Export"
    powerActiveImport = "Power.Active.Import"
    powerFactor = "Power.Factor"
    powerOffered = "Power.Offered"
    powerReactiveExport = "Power.Reactive.Export"
    powerReactiveImport = "Power.Reactive.Import"
    soc = "SoC"
    temperature = "Temperature"
    voltage = "Voltage"


class MessageTriggerEnumType:
    """
    Type of request to be triggered in a TriggerMessage.req
    """

    bootNotification = "BootNotification"
    logStatusNotification = "LogStatusNotification"
    firmwareStatusNotification = "FirmwareStatusNotification"
    heartbeat = "Heartbeat"
    meterValues = "MeterValues"
    signChargingStationCertificate = "SignChargingStationCertificate"
    signV2GCertificate = "SignV2GCertificate"
    statusNotification = "StatusNotification"
    transactionEvent = "TransactionEvent"


class PhaseEnumType:
    """
    Phase as used in SampledValue. Phase specifies how a measured value is to
    be interpreted. Please note that not all values of Phase are applicable to
    all Measurands.
    """

    l1 = "L1"
    l2 = "L2"
    l3 = "L3"
    n = "N"
    l1n = "L1-N"
    l2n = "L2-N"
    l3n = "L3-N"
    l1l2 = "L1-L2"
    l2l3 = "L2-L3"
    l3l1 = "L3-L1"


class ReadingContextEnumType:
    """
    Values of the context field of a value in SampledValue.
    """

    interruptionBegin = "Interruption.Begin"
    interruptionEnd = "Interruption.End"
    other = "Other"
    sampleClock = "Sample.Clock"
    samplePeriodic = "Sample.Periodic"
    transactionBegin = "Transaction.Begin"
    transactionEnd = "Transaction.End"
    trigger = "Trigger"


class ReasonEnumType:
    """
    Reason for stopping a transaction in StopTransaction.req.
    """

    emergencyStop = "EmergencyStop"
    evDisconnected = "EVDisconnected"
    local = "Local"
    localOutOfCredit = "LocalOutOfCredit"
    other = "Other"
    powerLoss = "PowerLoss"
    reboot = "Reboot"
    remote = "Remote"
    unlockCommand = "UnlockCommand"
    deAuthorized = "DeAuthorized"
    sOCLimitReached = "SOCLimitReached"
    powerQuality = "PowerQuality"
    overcurrentFault = "OvercurrentFault"
    masterPass = "MasterPass"
    immediateReset = "ImmediateReset"
    groundFault = "GroundFault"
    energyLimitReached = "EnergyLimitReached"
    stoppedByEV = "StoppedByEV"
    timeLimitReached = "TimeLimitReached"
    timeout = "Timeout"


class RecurrencyKindEnumType:
    """
    "Daily": The schedule restarts at the beginning of the next day.
    "Weekly": The schedule restarts at the beginning of the next week
              (defined as Monday morning)
    """

    daily = "Daily"
    weekly = "Weekly"


class RegistrationStatusEnumType:
    """
    Result of registration in response to BootNotification.req.
    """

    accepted = "Accepted"
    pending = "Pending"
    rejected = "Rejected"


class RemoteStartStopStatus:
    """
    The result of a RemoteStartTransaction.req or RemoteStopTransaction.req
    request.
    """
    accepted = "Accepted"
    rejected = "Rejected"


class ReserveNowStatusEnumType:
    """
    Status in ReserveNow.conf.
    """

    accepted = "Accepted"
    faulted = "Faulted"
    occupied = "Occupied"
    rejected = "Rejected"
    unavailable = "Unavailable"


class ResetStatusEnumType:
    """
    Result of Reset.req
    """

    accepted = "Accepted"
    rejected = "Rejected"
    scheduled = "Scheduled"


class TriggerMessageStatusEnumType:
    """
    Status in TriggerMessage.conf.
    """

    accepted = "Accepted"
    rejected = "Rejected"
    notImplemented = "NotImplemented"


class UnitOfMeasure:
    """
    Allowable values of the optional "unit" field of a Value element, as used
    in MeterValues.req and StopTransaction.req messages. Default value of
    "unit" is always "Wh".
    """

    wh = "Wh"
    kwh = "kWh"
    varh = "varh"
    kvarh = "kvarh"
    w = "W"
    kw = "kW"
    va = "VA"
    kva = "kVA"
    var = "var"
    kvar = "kvar"
    a = "A"
    v = "V"
    celsius = "Celsius"
    fahrenheit = "Fahrenheit"
    k = "K"
    percent = "Percent"


class UnlockStatusEnumType:
    """
    Status in response to UnlockConnector.req.
    """

    unlocked = "Unlocked"
    unlockFailed = "UnlockFailed"


class UpdateStatusEnumType:
    """
    Type of update for a SendLocalList.req.
    """

    accepted = "Accepted"
    failed = "Failed"
    versionMismatch = "VersionMismatch"


class UpdateEnumType:
    """
    Type of update for a SendLocalList.req.
    """

    differential = "Differential"
    full = "Full"


class ValueFormat:
    """
    Format that specifies how the value element in SampledValue is to be
    interpreted.
    """

    raw = "Raw"
    signedData = "SignedData"
