#include <stdio.h>
#include <stdlib.h>

#define MAX 100

int visited[MAX] = {0}; // Array to keep track of visited nodes
int graph[MAX][MAX];    // Adjacency matrix
int n;                  // Number of vertices

void DFS(int vertex) {
    printf("%d ", vertex);
    visited[vertex] = 1;

    for (int i = 0; i < n; i++) {
        if (graph[vertex][i] == 1 && !visited[i]) {
            DFS(i);
        }
    }
}

int main() {
    int edges, u, v;

    printf("Enter the number of vertices: ");
    scanf("%d", &n);

    printf("Enter the number of edges: ");
    scanf("%d", &edges);

    printf("Enter the edges (u v):\n");
    for (int i = 0; i < edges; i++) {
        scanf("%d %d", &u, &v);
        graph[u][v] = 1;
        graph[v][u] = 1; // For undirected graph
    }

    printf("DFS Traversal: ");
    DFS(0); // Assuming 0 as the starting vertex

    return 0;
}
