from DirectedGraph import DirectedGraph

class DirectedPath(object):

    def __init__(self, graph, vertex):
        self.__origin = vertex
        self.__graph = graph
        self.__reachable = []
        self.__edgeTo = []
        for i in range(0,graph.Size()):
            self.__reachable.append(False)
            self.__edgeTo.append(None)
        self.Search()
        print self.__reachable, self.__edgeTo

    def __depthFirstSearch(self, origin):
        if origin not in self.__graph.vertices:
            return None
        adjList = self.__graph.getAdj(origin)
        originIdx = self.__graph.vertices.index(origin)
        self.__reachable[originIdx] = True
        for vertexIdx in adjList:
            print "From %d to %d",(origin,self.__graph.vertices[vertexIdx])
            #Did we already visit this vertex?
            if not self.__reachable[vertexIdx]:
                self.__edgeTo[vertexIdx] = originIdx
                self.__depthFirstSearch(self.__graph.vertices[vertexIdx])

    def Search(self):
        self.__depthFirstSearch(self.__origin)
        return

    def hasPathTo(self, vertex):
        if vertex not in self.__graph.vertices:
            return False
        return self.__reachable[self.__graph.vertices.index(vertex)]

    def pathTo(self, vertex):
        vertexIdx = self.__graph.vertices.index(vertex)
        path = []
        if not self.__reachable[vertexIdx]:
            return []
        path.append(vertexIdx)
        # If we visited vertex then there's definitely a path
        # traverse back from vertex to origin
        while self.__edgeTo[vertexIdx] != None:
            path.append(self.__edgeTo[vertexIdx])
            vertexIdx = self.__edgeTo[vertexIdx]

        return [self.__graph.vertices[node] for node in path][::-1]

####
#d = DirectedGraph([1,12,15,4,2])
#d.addEdge(1,12)
#d.addEdge(15, 4)
#d.addEdge(12,15)
#d.addEdge(12,4)
#d.addEdge(4,1)
#dPath = DirectedPath(d,1)
#print dPath.hasPathTo(2)
#print dPath.hasPathTo(15)
#print dPath.pathTo(2)
