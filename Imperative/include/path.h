
#ifndef _ALGO_PATH_H_
#define _ALGO_PATH_H_

#include <graph.h>
typedef struct _path{
	graph *graph;
	vertex *edgeTo;
	int *visited;
	vertex origin;
} path;

path *pathInit(graph *, vertex);
int hasPathTo(path *, vertex);
size_t pathTo(path *, vertex, vertex *); 


#endif
