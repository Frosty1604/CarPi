import time

import obd

from reader import Reader


# obd.logger.setLevel(obd.logging.DEBUG)

connection = obd.OBD("/dev/ttys001")

# response_SPEED = connection.query(obd.commands.SPEED)
# response_RUN_TIME = connection.query(obd.commands.RUN_TIME)
# response_RPM = connection.query(obd.commands.RPM)
# response_THROTTLE_POS = connection.query(obd.commands.THROTTLE_POS)
# response_FUEL_TYPE = connection.query(obd.commands.FUEL_TYPE)
# response_FUEL_RATE = connection.query(obd.commands.FUEL_RATE)

# while True:
#     response_SPEED = connection.query(obd.commands.SPEED)
#     response_RUN_TIME = connection.query(obd.commands.RUN_TIME)
#     response_RPM = connection.query(obd.commands.RPM)
#     response_THROTTLE_POS = connection.query(obd.commands.THROTTLE_POS)
#     response_FUEL_TYPE = connection.query(obd.commands.FUEL_TYPE)
#     response_DTC = connection.query(obd.commands.GET_DTC)
#
#     print("------------------------")
#     print
#     print(response_SPEED)
#     print(response_RUN_TIME)
#     print(response_THROTTLE_POS)
#     print(response_RPM)
#     print(response_FUEL_TYPE)
#     print(response_DTC)
#     print()
#     print("------------------------")
#     time.sleep(1)

reader = Reader("/dev/ttys001")

def get_data():
    while True:
        print(reader.get_speed())
        print(reader.get_rpm())
        print(reader.get_engine_load())
        print(reader.get_engine_run_time())
        time.sleep(0.2)
        print("-----------------------------")

print(connection.status())
# print(obd.commands.SPEED)

if __name__ == '__main__':
    get_data()