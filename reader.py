import obd

import database_manager
import datetime

logger_commands = {
    "speed": obd.commands.SPEED,
    "rpm": obd.commands.RPM,
    "throttle_pos": obd.commands.THROTTLE_POS,
    "coolant_temp": obd.commands.COOLANT_TEMP,
    # "fuel_status": obd.commands.FUEL_STATUS,
    # "engine_load": obd.commands.ENGINE_LOAD,
    # "fuel_rate": obd.commands.FUEL_RATE,
    # "oil_temp": obd.commands.OIL_TEMP,
    # "intake_temp": obd.commands.INTAKE_TEMP,
}


class Reader:
    __instance = None

    def __init__(self, port: str):
        self.connection = obd.OBD(port, fast=False)
        database_manager.create_table()
        Reader.__instance = self

    @staticmethod
    def get_instance(port: str):
        """ Static access method. """
        if not Reader.__instance:
            Reader(port)
        return Reader.__instance

    def get_data(self, command):
        try:
            return self.connection.query(command).value.magnitude
        except Exception as e:
            print(e)
            return self.connection.query(command).value

    def get_speed(self):
        return self.connection.query(obd.commands.SPEED)

    def get_rpm(self):
        return self.connection.query(obd.commands.RPM)

    def get_engine_run_time(self):
        return self.connection.query(obd.commands.RUN_TIME)

    def get_throttle_position(self):
        return self.connection.query(obd.commands.THROTTLE_POS)

    def get_fuel_level(self):
        return self.connection.query(obd.commands.FUEL_LEVEL)

    def get_status(self):
        return self.connection.query(obd.commands.STATUS)

    def get_coolant_temp(self):
        return self.connection.query(obd.commands.COOLANT_TEMP)

    def get_fuel_status(self):
        return self.connection.query(obd.commands.FUEL_STATUS)

    def get_engine_load(self):
        return self.connection.query(obd.commands.ENGINE_LOAD)

    def get_fuel_type(self):
        return self.connection.query(obd.commands.FUEL_TYPE)

    def get_fuel_rate(self):
        return self.connection.query(obd.commands.FUEL_RATE)

    def get_oil_temp(self):
        return self.connection.query(obd.commands.OIL_TEMP)

    def get_intake_temp(self):
        return self.connection.query(obd.commands.INTAKE_TEMP)

    def get_maf(self):
        return self.connection.query(obd.commands.MAF)

    def get_elm_version(self):
        return self.connection.query(obd.commands.ELM_VERSION)

    def get_elm_voltage(self):
        return self.connection.query(obd.commands.ELM_VOLTAGE)

    def get_all(self):
        data_all = ["Speed: " + str(self.get_speed()), "RPM: " + str(self.get_rpm()),
                    "Engine Runtime: " + str(self.get_engine_run_time()),
                    "Throttle Position: " + str(self.get_engine_run_time()),
                    "Fuel Level: " + str(self.get_fuel_level()), "Fuel Type: " + str(self.get_fuel_type()),
                    "Fuel Rate: " + str(self.get_fuel_rate()), "Oil Temp: " + str(self.get_oil_temp()),
                    "Coolant Temp: " + str(self.get_coolant_temp()), "Intake Temp: " + str(self.get_intake_temp()),
                    "Engine Load: " + str(self.get_engine_load()), "MAF: " + str(self.get_maf()),
                    "Status: " + str(self.get_status())]
        return data_all

    def get_data_for_db(self):
        data = [
            str(datetime.datetime.now().timestamp()),
            str(self.get_speed()), #speed
            str(self.get_rpm()),   #rpm
            str(self.get_engine_run_time()), #engine runtime
            str(self.get_throttle_position()), #throttle pos
            str(self.get_fuel_level()), # fuel level
            str(self.get_fuel_rate()), # fuel rate
            str(self.get_coolant_temp()), #coolant temp
            str(self.get_oil_temp()), #oil temp
            str(self.get_engine_load()), #engine load
        ]

        return data

    def logger(self):
        database_manager.add_data(self.get_data_for_db())
        print("logged data")

    def is_connected(self):
        return self.connection.is_connected()
