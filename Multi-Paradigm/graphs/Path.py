from Graph import Graph
from Queue import Queue
import random

class Path():
	# Generic data structure
	__graph = None
	__edgeTo = []
	__oldVertices = []
	# depth first execlusive
	__visited = []
	__origin = None
	def __init__(self, graph, vertex):
		if not isinstance(graph, Graph):
			return None
		if graph.getIndex(vertex) == None:
			return None
		self.__origin = vertex
		self.__graph = graph
		for i in self.__graph.vertices:
			self.__oldVertices.append(i)
		for i in range(0, graph.Size()):
			self.__visited.append(False)
			self.__edgeTo.append(None)
		self.Search()
	def __breadthFirst(self,s):
		q = Queue()
		depth = 0
		q.put(s)
		self.__visited[self.__graph.getIndex(s)] = True

		while not q.empty():
			v = q.get()
			for i in self.__graph.Adj(v):
				if self.__visited[self.__graph.getIndex(i)] == False:
					q.put(i)
					self.__visited[self.__graph.getIndex(i)] = True
					self.__edgeTo[self.__graph.getIndex(i)] = v
		return

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
		#self.__depthFirst(self.__origin)
		self.__breadthFirst(self.__origin)
	#if we've been there there's definitely a path

	def Update(self):
		x = self.__graph.Size() - len(self.__visited)
		count = 0
		oldLen = len(self.__visited)
		# Compare old vertices to new ones
		# Adjust visited and edgeToList to it
		# Make a search
		if x != 0:
			# Extend Aux data structures
			self.__visited = []
			self.__edgeTo = []
			for i in range(0,len(self.__graph.vertices)):
				self.__visited.append(False)
				self.__edgeTo.append(None)
			self.Search()
	def hasPathTo(self,vertex):
		return self.__visited[self.__graph.getIndex(vertex)]

	#return array of vertexes to go through
	# Loop implementation to find Path
	# to work on big graphs
	# Thanks python recursion limit...
	def pathTo(self,vertex):
		x = []
		if self.__visited[self.__graph.getIndex(vertex) ] == False:
			return x

		x.append(vertex)
		i = self.__graph.getIndex(vertex)
		while self.__edgeTo[i] != None:
			x.append(self.__edgeTo[i])
			i = self.__graph.getIndex(self.__edgeTo[i])
		x.reverse()
		return x

	# Recursive version of find Path
	# doesn't work on big graphs
	# Recursion in python limited
	# to 990
	def rpathTo(self,vertex):
		if self.__edgeTo[self.__graph.getIndex(vertex)] == None and not self.__visited[self.__graph.getIndex(vertex)]:
			return [None]
		elif self.__edgeTo[self.__graph.getIndex(vertex)] == None and self.__visited[self.__graph.getIndex(vertex)]:
			return [vertex]
			#if no path then we cannot append to None
		x = self.rpathTo(self.__edgeTo[self.__graph.getIndex(vertex)])
		x.append(vertex)
		return x

g = Graph([1,2,3,4,5,7])
g.addEdge(1,2)
g.addEdge(3,2)
g.addEdge(4,3)
g.addEdge(7,5)
g.addEdge(4,5)
g.addEdge(4,7)
p = Path(g,1)
g.addVertex(6)
g.addEdge(6,7)
p.Update()
print p.hasPathTo(6)
print p.pathTo(6)
