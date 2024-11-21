class Room:
    def __init__(self, name):
        self.name = name
        self.connections=[]
    def addConnection(self, connection):
        self.connections.append(connection)
        connection.destination.connections.append(self)

class Connection:
    def __init__(self, destination):
        self.destination = destination

Vegas = Room("Vegas")
NightCity = Room("Night City")
Toyko = Room("Toyko")

Vegas.addConnection(Connection(NightCity))
Vegas.addConnection(Connection(Toyko))

for connection in Vegas.connections:
    print(connection.destination.name)

for connection in NightCity.connections:
    print(connection.name)

