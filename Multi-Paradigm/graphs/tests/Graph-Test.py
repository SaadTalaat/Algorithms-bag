
import unittest
from Graph import Graph
class GraphTest(unittest.TestCase):
	graph = None
	adj = None
	mutex = 0
	def setUp(self):
		if self.mutex == 0:
			self.graph = Graph([1,2,3,4,6])
			self.graph.addEdge(1,3)
			self.graph.addEdge(2,4)
			self.graph.addEdge(2,6)
			self.graph.addEdge(6,4)
			self.adj = self.graph.getAdj()
		self.mutex = 1

	def tearDown(self):
		self.graph = None

	def testDegree (self):

		assert self.graph.degree(1) == len(self.adj[0]), 'degree = x\n'
		assert self.graph.degree(4) == len(self.adj[3]), 'degree = x\n'

	def testMaxDegree(self):
		assert self.graph.maxDegree() == len(self.adj[4]), 'max degree = x\n'

	def testAvgDegree(self):
		assert self.graph.avgDegree() == (sum(map(len,self.adj))/2), 'avg degree = \n'

	def testSelfLoops(self):
		#assert self.graph.selfLoops() == , 'self loops = %d' % self.graph.selfLoops()
		return

if __name__ == "__main__":
	unittest.main()
