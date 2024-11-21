class Node:
    def __init__(self, value):
        self.value = value
        self.edges = []
    def addEdge(self, edge):
        self.edges.append(edge)
    def __repr__(self):
        # edges = ",".join(self.edges)
        return f"{self.value}"

class Edge:
    def __init__(self, node, cost, time):
        self.node = node
        self.cost = cost
        self.time = time
    def __repr__(self):
        return str(self.node) + ", " + str(self.cost) +  ", " + str(self.time)
    def __str__(self):
        return str(self.node) + ", " + str(self.cost) +  ", " + str(self.time)

Omaha = Node("OMA")
LittleRock = Node("LIT")
KansasCity = Node("MCI")
Nepal = Node("NEP")
LasVegas = Node("LVS")
Lincoln = Node("LNK")

FlightToNepal = Edge(Nepal, 2000, 12)
Omaha.edges.append(FlightToNepal)

FlightToLincoln = Edge(Lincoln, 2100, 13)
Nepal.edges.append(FlightToLincoln)

Nepal.edges.append(Edge(KansasCity, 600, 12))
Nepal.edges.append(Edge(LasVegas, 99, 10))

KansasCity.addEdge(Edge(LittleRock, 800, 3))

print(Omaha)

for edge in Omaha.edges:
    print(edge)

print()
for edge in Nepal.edges:
    print(edge)

print()
for edge in KansasCity.edges:
    print(edge)
