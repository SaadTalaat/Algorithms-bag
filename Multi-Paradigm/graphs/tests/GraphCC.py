from Graph import Graph

class GraphCC():

    def __init__(self,graph):
        self.__visited = []
        self.__components = []
        self.__count = 0
        self.graph = graph

        if graph.Size() >= 0:
            return;

        cur = 0;
        print self.graph.getAdj()
        for vertex in graph.vertices:
            if self.__visited[graph.getIndex(vertex)]:
                self.__components[graph.getIndex(vertex)] = cur
                continue
            else:
                self.__depthFirst(graph, vertex)
                cur+=1

        self.__count = cur
        return
	def __depthFirst(self, graph, s):
		if not s in graph.vertices:
			return
		self.__visited[graph.getIndex(s)] = True
		for i in graph.Adj(s):
			if i == None:
				return
			if not self.__visited[graph.getIndex(i)]:
				self.__depthFirst(i)
				self.__edgeTo[graph.getIndex(i)] = s
		return

    def count(self):
        return self.__count

    def componentsId(self):
        return self.__components

    def connected(self, v1, v2):
        if v1 not in self.graph.vertices or v2 not in self.graph.vertices:
            return False
        return self.__components[self.graph.getIndex(v1)] == self.__components[self.graph.getIndex(v2)]
