import obd

from database_manager import DatabaseManager

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

    def __init__(self, port: str, database_name: str):
        self.connection = obd.OBD(port, fast=False)
        self.database_manager = DatabaseManager(database_name)
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

    def init_logger(self):
        for key in logger_commands.keys():
            self.database_manager.create_table(key)

    def logger(self):
        for command in logger_commands:
            self.database_manager.add_data(command, self.get_data(logger_commands.get(command)))
        print("logged data")

    def is_connected(self):
        return self.connection.is_connected()
