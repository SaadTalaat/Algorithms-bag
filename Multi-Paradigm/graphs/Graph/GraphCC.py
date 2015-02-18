from Graph import Graph

class GraphCC():

    def __init__(self,graph):
        self.__visited = []
        self.__components = []
        self.__count = 0
        self.graph = graph

        if graph.Size() <= 0:
            return;
        for i in range(0,graph.Size()):
            self.__visited.append(False)
            self.__components.append(-1)

        for vertex in graph.vertices:
            if self.__visited[graph.getIndex(vertex)]:
                continue
            else:
                self.__depthFirst(graph, vertex)
                self.__count +=1

        return

    def __depthFirst(self, graph, s):
        if not s in graph.vertices:
            return
        self.__visited[graph.getIndex(s)] = True
        self.__components[graph.getIndex(s)] = self.__count
        for i in graph.Adj(s):
            if i == None:
                return
            if not self.__visited[graph.getIndex(i)]:
                self.__depthFirst(g,i)
                self.__components[graph.getIndex(i)] = self.__count
        return

    def count(self):
        return self.__count

    def componentsId(self):
        return self.__components

    def connected(self, v1, v2):
        if v1 not in self.graph.vertices or v2 not in self.graph.vertices:
            return False
        return self.__components[self.graph.getIndex(v1)] == self.__components[self.graph.getIndex(v2)]

g = Graph([1,2,3,4,13,12,6])
g.addEdge(1,3)
g.addEdge(2,4)
g.addEdge(2,6)
g.addEdge(6,4)
g.addEdge(13,12)
print g.getAdj()
cc = GraphCC(g)
print cc.count()
print cc.componentsId()
print cc.connected(12,13)
