
class DirectedGraph(object):

    def __init__(self, vertices):
        assert type(vertices) == type([])
        self.vertices = vertices
        self.__adj = []
        for v in vertices:
            self.__adj.append([])

    def addEdge(self, v1, v2):
        if type(v1) != type(v2) or v1 not in self.vertices or v2 not in self.vertices:
            return False
        self.__adj[self.vertices.index(v1)].append(self.vertices.index(v2))
        return True

    def addVertex(self, v):
        self.vertices.append(v)
        return True

    def getAdj(self, v):
        if v not in self.vertices:
            return None
        return self.__adj[self.vertices.index(v)]

    def Adj(self):
        return self.__adj

    def getIndex(self, v):
        if v not in self.vertices:
            return -1
        return self.vertices.index(v)

    def Size(self):
        return len(self.vertices)


    def selfLoops(self):
        count = 0
        # loop by index since V value doesn't matter for us
        for v in range(0,len(self.vertices)):
            if v in self.__adj[v]:
                count+=1
        return count
