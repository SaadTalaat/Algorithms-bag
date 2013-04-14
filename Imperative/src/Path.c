#include <stdio.h>
#include <stdlib.h>
#include <graph.h>
#include <binary.h>
#include <path.h>


static void
__initPathes(path *, vertex);

path *
pathInit(graph *graph, vertex origin)
{
	int i;
	path *p;
	if (graph == NULL)
		return NULL;
	if( BinarySearch(graph->vertices, origin, graph->vertCount)== -1)
		return NULL;
	p = (path *) malloc(sizeof(path));
	p->graph = graph;
	p->edgeTo = (vertex *) malloc(graph->vertCount*sizeof(vertex));
	p->visited = (int *) malloc(graph->vertCount*sizeof(int));
	p->origin = origin;

	for(i = 0; i < graph->vertCount; i++)
		p->edgeTo[i] = 0;
		p->visited[i] = 0;
	__initPathes(p, origin);
}

int
hasPathTo(path *p, vertex dest)
{
	int index;
	index = BinarySearch(p->graph->vertices, dest, p->graph->vertCount);
	if(index == -1)
		return 0;
	return p->visited[index];
}

size_t
pathTo(path *p, vertex dest, vertex *stack)
{
	int index,count = 0;
	int origin,i;
	if(stack == NULL || p == NULL)
		return 0;

	index = BinarySearch(p->graph->vertices, dest, p->graph->vertCount);
	origin = BinarySearch(p->graph->vertices, p->origin, p->graph->vertCount);

	if( p->edgeTo[index] == 0 && p->visited[index] != 1)
		// we've never been there then!!
		return 0;
	for(i = index; i != origin; i = BinarySearch(p->graph->vertices, p->edgeTo[index], p->graph->vertCount))
	{
		stack[count] = p->graph->vertices[i];
	}
	
	return count;
}

static void
__initPathes(path *p, vertex dest)
{
	vertex *s;
	int i,index, index2;
	vertex *adjList;
	if(p == NULL)
		return;
	index = BinarySearch(p->graph->vertices, dest, p->graph->vertCount);
	if(index == -1)
		return;

	p->visited[index] = 1;
	adjList = getAdj(p->graph, dest);

	for (i = 0; i < p->graph->adjSize[index]; i++)
	{
		if (adjList[i] == 0)
			return;
		// Impossible to happend
		index2 = BinarySearch(p->graph->vertices, adjList[i], p->graph->vertCount);
		if(p->visited[index2] == 1 )
			return;
		else
		{
			p->visited[index2] = 1;
			__initPathes(p, adjList[i]);
			p->edgeTo[index2] = dest;
		}
	}
	
}
