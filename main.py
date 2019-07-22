import time

import obd

from reader import Reader

# obd.logger.setLevel(obd.logging.DEBUG)

connection = obd.OBD("/dev/ttys001")

reader = Reader("/dev/ttys002")

import database_manager


def get_data():
    while True:
        print(reader.get_speed())
        print(reader.get_rpm())
        print(reader.get_engine_load())
        print(reader.get_engine_run_time())
        time.sleep(0.2)
        print("-----------------------------")


print(connection.status())

if __name__ == '__main__':
    database_manager.create_table()
    while True:
        reader.logger()
        time.sleep(1)
