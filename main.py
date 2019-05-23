import obd

connection = obd.OBD()

response = connection.query(obd.commands.SPEED)
print(response)
print(connection.status())
# print(obd.commands.SPEED)
