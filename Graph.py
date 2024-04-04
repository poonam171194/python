import pprint

class vertax:
    def __init__(self, name):
        self.name = name
        self.connections = []
    
    def add_edge(self,obj):
        self.connections.append(obj)


class Edges:
    def __init__(self):
        self.connections = []
    
    def add_edge(self,from_ver, To_ver):
        self.connections.append(from_ver.name)
        self.connections.append(To_ver.name)


class Graph:
    def __init__(self):
        self.graph = {}

    def add_vertices(self,obj):
        self.graph.update({obj.name:obj.connections})

v1 = vertax("1")
v2 = vertax("2")
v3 = vertax("3")
v4 = vertax("4")
v5 = vertax("5")

e1 = Edges()
e1.add_edge(v1,v2)

e2 = Edges()
e2.add_edge(v1,v3)

e3 = Edges()
e3.add_edge(v3,v2)

e4 = Edges()
e4.add_edge(v1,v4)

e5 = Edges()
e5.add_edge(v2,v5)

e6 = Edges()
e6.add_edge(v4,v5)

#v1
v1.add_edge(e1.connections)
v1.add_edge(e2.connections)
v1.add_edge(e4.connections)

#v2
v2.add_edge(e5.connections)
v2.add_edge(e3.connections)
v2.add_edge(e1.connections)

#v3
v3.add_edge(e2.connections)
v3.add_edge(e3.connections)

#v4
v4.add_edge(e4.connections)
v4.add_edge(e6.connections)

#v5
v5.add_edge(e5.connections)
v5.add_edge(e6.connections)

#Graph add

G1 = Graph()

G1.add_vertices(v1)
G1.add_vertices(v2)
G1.add_vertices(v3)
G1.add_vertices(v4)
G1.add_vertices(v5)

pprint.pprint(G1.graph)