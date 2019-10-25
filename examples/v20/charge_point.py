import asyncio

try:
    import websockets
except ModuleNotFoundError:
    print("This example relies on the 'websockets' package.")
    print("Please install it by running: ")
    print()
    print(" $ pip install websockets")
    import sys
    sys.exit(1)

from ocpp.v16.enums import RegistrationStatus
from ocpp.v20 import call

from ocpp.charge_point import ChargePoint as cp

#from ocpp.v16.enums import RegistrationStatus


class ChargePoints(cp):
    async def send_boot_notification(self):
        request = call.BootNotificationPayload(
            charging_station= 'TMH_000001',
            reason= 'PowerUp'
        )

        response = await self.call(request)

        if response.status ==  RegistrationStatus.accepted:
            print("Connected to central system.")


async def main():
    async with websockets.connect(
        'ws://localhost:9000/CP_1',
         subprotocols=['ocpp2.0']
    ) as ws:

        cp = ChargePoints('CP_1', ws, '2.0')

        await asyncio.gather(cp.start(), cp.send_boot_notification())


if __name__ == '__main__':
    try:
        # asyncio.run() is used when running this example with Python 3.7 and
        # higher.
        asyncio.run(main())
    except AttributeError:
        # For Python 3.6 a bit more code is required to run the main() task on
        # an event loop.
        loop = asyncio.get_event_loop()
        loop.run_until_complete(main())
        loop.close()
