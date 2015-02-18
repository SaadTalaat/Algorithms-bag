#Basic Graph implementaion
# using adjecency-list
#
class Graph(object):
	vertices = None
	adjList = []
	def __init__(self, vertices):
		try:
			assert  type(vertices) == type([])
		except:
			print "Type error: Input should be array of vertices"

		self.vertices = vertices
		for i in range(0,len(vertices)):
			self.adjList.append([]);
		return

	def addEdge(self, vertex1, vertex2):
		if (not ( vertex1 in self.vertices)) or (not (vertex2 in self.vertices)):
			return 
		self.adjList[self.vertices.index(vertex1)].append(vertex2)
		self.adjList[self.vertices.index(vertex2)].append(vertex1)

	def addVertex(self, vertex):
		if vertex in self.vertices:
			return False
		self.vertices.append(vertex)
		self.vertices.sort()
		self.adjList.append([])
		return True	

	def degree(self, vertex):
		if not(vertex in self.vertices):
			return 0
		return len(self.adjList[vertex-1])

	def maxDegree(self):
		return max( map(len,self.adjList));

	def avgDegree(self):
		return ( sum(map(len,self.adjList)) / len(self.vertices))

	def selfLoops(self):
		countv = 0
		for i in range (0,len(self.vertices)):
			countv += self.adjList[i].count(self.vertices[i])

		return countv/2
	def getAdj(self):
		return self.adjList

	def Size(self):
		return len(self.vertices)

	def Adj(self, vertex):
		try:
			assert vertex in self.vertices
		except:
			return None
		return self.adjList[self.vertices.index(vertex)]
	def getIndex(self, vertex):
		if vertex in self.vertices:
			return self.vertices.index(vertex)

