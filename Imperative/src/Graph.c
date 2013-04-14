#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <binary.h>
#include <graph.h>


/**
 * Initalizes a graph with empty adjList
 */
graph*
graphInit(vertex *vertices, size_t vert_count)
{

	if(vertices == NULL || vert_count == 0)
		return;
	graph *g;
	// allocate space for a graph
	g = (graph *) malloc(sizeof(graph));
	memset(g,0,sizeof(graph));

	// allocate a space for each vertices
	g->vertices = (unsigned int *) malloc(vert_count*sizeof(unsigned int));
	memcpy(g->vertices,vertices, vert_count*sizeof(unsigned int));
	
	// allocate a pointer for each vertex adjList
	g->adjList = (vertex **) malloc(sizeof(void *)*vert_count);
	memset(g->adjList,0,sizeof(void *)*vert_count);

	g->adjSize = (unsigned int*) malloc(vert_count*sizeof(unsigned int));
	memset(g->adjSize, 0, vert_count*sizeof(unsigned int));

	g->vertCount = vert_count;
	return g;
}
vertex *
getAdj(graph *g, vertex v)
{
	int ss;
	ss = BinarySearch(g->vertices, v, g->vertCount);
	if(ss == -1)
		return NULL;
	return g->adjList[ss];
}

void
addEdge(graph *g, vertex v1, vertex v2)
{
	unsigned int *a;
	unsigned int i,j;
	if(g == NULL)
		return;

	i = BinarySearch(g->vertices, v1, g->vertCount);
	j = BinarySearch(g->vertices, v2, g->vertCount);

	if(i == -1 || j == -1)
	{
		return;
	}
	if(g->adjList[i] == NULL)
	{
		// initalize list size with one entry position
		g->adjList[i] = (unsigned int *) malloc(sizeof(unsigned int));
		g->adjSize[i] = 1;
	//	printf("AdjList of %d = %d\n",i,v2);
		g->adjList[i][0] = v2;
	}
	else
	{
		a = g->adjList[i];
		//allocate new heap with same size + 1
		g->adjList[i] = malloc( (g->adjSize[i]*sizeof(unsigned int)) + sizeof(unsigned int));
		memcpy(g->adjList[i], a, g->adjSize[i]*sizeof(unsigned int));
		free(a);
		g->adjList[i][g->adjSize[i]] = v2;
		g->adjSize[i] ++;
	}
        if(g->adjList[j] == NULL)
        {
                // initalize list size with one entry position
                g->adjList[j] = (unsigned int *) malloc(sizeof(unsigned int));
                g->adjSize[j] = 1;
                g->adjList[j][0] = v1;
        }
        else    
        {
                a = g->adjList[j];
                //allocate new heap with same size + 1
                g->adjList[j] = malloc( (g->adjSize[j]*sizeof(unsigned int)) + sizeof(unsigned int));
                memcpy(g->adjList[j], a, g->adjSize[j]*sizeof(unsigned int));
                free(a);
                g->adjList[j][g->adjSize[j]] = v1;
                g->adjSize[j] ++;
        }

}

int
vectDegree(graph *g, vertex v)
{
	int i;
	if(g == NULL)
		return;
	i = BinarySearch(g->vertices, v, g->vertCount);
	if( i == -1)
	{
		printf("Invalid\n");
		return -1;
	}
	return g->adjSize[i];
}

int
maxDegree(graph *g)
{
	int i, max;
	if( g == NULL)
		return;
	max = 0;
	for(i = 0; i < g->vertCount; i++)
		if( g->adjSize[i] != 0 && g->adjSize[i] > max)
			max = g->adjSize[i];

	return max;
}

int
avgDegree(graph *g)
{
	int i, sum;
	if(g == NULL)
		return;
	sum = 0;
	for(i =0; i< g->vertCount; i++)
		if( g->adjSize[i] != 0)
			sum += g->adjSize[i];
	return (sum/g->vertCount);
}

int
selfLoops(graph *g)
{
	int i,j,count=0;
	vertex v,a;
	if(g == NULL)
		return -1;
	for(i = 0,v = g->vertices[i]; i < g->vertCount; i++,v = g->vertices[i])
		if(g->adjList[i] != NULL)
			for( j=0,a=g->adjList[i][j]; j < g->adjSize[i]; j++,a=g->adjList[i][j])
			{
				if(v == a)
				{
					count++;
				}
			}
	return count;
}
