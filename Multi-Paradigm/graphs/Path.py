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
		if graph.getIndex(vertex) == None:
			return None
		self.__origin = vertex
		self.__graph = graph
		for i in range(0, graph.Size()):
			self.__visited.append(False)
			self.__edgeTo.append(None)
		self.Search()
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

	#if we've been there there's definitely a path
	def hasPathTo(self,vertex):
		return self.__visited[self.__graph.getIndex(vertex)]

	#return array of vertexes to go through
	def pathTo(self,vertex):
		if self.__edgeTo[self.__graph.getIndex(vertex)] == None and not self.__visited[self.__graph.getIndex(vertex)]:
			return [None]
		elif self.__edgeTo[self.__graph.getIndex(vertex)] == None and self.__visited[self.__graph.getIndex(vertex)]:
			return [vertex]
			#if no path then we cannot append to None
		x = self.pathTo(self.__edgeTo[self.__graph.getIndex(vertex)])
		x.append(vertex)
		return x

