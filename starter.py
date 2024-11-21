class Node:
    def __init__(self, value):
        self.value = value
        self.edges = []

    def addEdge(self, edge):
        self.edges.append(edge)

    def __str__(self):
        # edges = ",".join([str(x) for x in self.edges])
        return f"{self.value}"

class Edge:
    def __init__(self, node):
        self.node = node
    def __str__(self):
        return str(self.node)

Omaha = Node("OMA")
LittleRock = Node("LIT")
KansasCity = Node("MCI")
Nepal = Node("NEP")
LasVegas = Node("LVS")
Lincoln = Node("LNK")

FlightToNepal = Edge(Nepal)
Omaha.edges.append(FlightToNepal)

FlightToLincoln = Edge(Lincoln)
Nepal.edges.append(FlightToLincoln)

Nepal.edges.append(Edge(KansasCity))
Nepal.edges.append(Edge(LasVegas))

KansasCity.addEdge(Edge(LittleRock))

print(Omaha)
print()
print("From Omaha I can go to: ")

for edge in Omaha.edges:
    print(edge)

print()
print("From Nepal I can go to:")
for edge in Nepal.edges:
    print(edge)

print()
print("FRom Kansas City I can go to:")
for edge in KansasCity.edges:
    print(edge)
