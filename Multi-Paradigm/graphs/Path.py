from Graph import Graph
import random

class Path():

	__graph = None
	__edgeTo = []
	__visited = []
	__origin = None
	def __init__(self, graph, vertex):
		if not isinstance(graph, Graph):
			return None
		self.__origin = vertex
		for i in range(0, graph.Size()):
			self.__visited.append(False)
			self.__edgeTo.append(None)
			self.__graph = graph

	def __depthFirst(self, s):
		if not s in self.__graph.vertices:
			return
		self.__visited[self.__graph.getIndex(s)] = True
		for i in self.__graph.Adj(s):
			if i == None:
				return
			if not self.__visited[self.__graph.getIndex(i)]:
				self.__depthFirst(i)
				self.__edgeTo[self.__graph.getIndex(i)] = s
		return
	def Search(self):
		self.__depthFirst(self.__origin)

	def hasPathTo(self,vertex):
		x = False
		if self.__edgeTo[self.__graph.getIndex(vertex)] == None and not self.__visited[self.__graph.getIndex(vertex)]:
			print "Equals to None and not visited"
			return False
		elif self.__edgeTo[self.__graph.getIndex(vertex)] == None and self.__visited[self.__graph.getIndex(vertex)]:
			return True
		return self.hasPathTo(self.__edgeTo[self.__graph.getIndex(vertex)])
g = Graph(range(0,1000))

for i  in range(0,1000):
	g.addEdge(random.randint(0,1000),random.randint(0,1000))

p = Path(g,random.randint(0,1000))
p.Search()
x = p.hasPathTo(random.randint(0,1000))
print x
