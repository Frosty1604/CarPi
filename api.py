import json

import obd
from flask import Flask
from flask_restful import Api, Resource, reqparse

from reader import Reader

app = Flask(__name__)
api = Api(app)

commands = {
    "speed": obd.commands.SPEED,
    "rpm": obd.commands.RPM,
    "run_time": obd.commands.RUN_TIME,
    "throttle_pos": obd.commands.THROTTLE_POS,
    "fuel_level": obd.commands.FUEL_LEVEL,
    "status": obd.commands.STATUS,
    "coolant_temp": obd.commands.COOLANT_TEMP,
    "fuel_status": obd.commands.FUEL_STATUS,
    "engine_load": obd.commands.ENGINE_LOAD,
    "fuel_type": obd.commands.FUEL_TYPE,
    "fuel_rate": obd.commands.FUEL_RATE,
    "oil_temp": obd.commands.OIL_TEMP,
    "intake_temp": obd.commands.INTAKE_TEMP,
    "maf": obd.commands.MAF,
    "elm_voltage": obd.commands.ELM_VOLTAGE,
    "elm_version": obd.commands.ELM_VERSION
}


class Api(Resource):
    def __init__(self):
        self.reader = Reader.get_instance("/dev/ttys001")

    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument("data")
        args = parser.parse_args()
        print(args)

        if not args.get("data"):
            return "No request was given", 404

        requests = args.get("data").split(",")
        data = {}
        for i in range(len(requests)):
            if requests[i]:
                data.update({requests[i]: str(self.reader.get_data(commands.get(requests[i])))})

        if data:
            print(data)
            return json.dumps(data), 200
        return "No Data available", 404


api.add_resource(Api, "/api")
app.run()
