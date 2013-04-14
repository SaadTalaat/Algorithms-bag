
#ifndef _ALGO_GRAPH_H_
#define _ALGO_GRAPH_H_
typedef unsigned int vertex;
typedef struct _graph{
	vertex *vertices;
	unsigned int vertCount;
	vertex **adjList;
	unsigned int *adjSize;
} graph;

graph* graphInit(vertex *vertices, size_t vert_count);
void addEdge(graph *g, vertex v1, vertex v2);
int vectDegree(graph *g, vertex v);
int maxDegree(graph *g);
int avgDegree(graph *g);
int selfLoops(graph *g);

#endif
