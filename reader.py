import obd


class Reader:

    def __init__(self, port: str):
        self.connection = obd.OBD(port)

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

    def fuel_rate(self):
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
        data_all = []
