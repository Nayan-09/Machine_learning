#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

#define MAX 100

int graph[MAX][MAX] = {
    {0, 1, 1, 0},
    {1, 0, 1, 1},
    {1, 1, 0, 1},
    {0, 1, 1, 0}
};

int numVertices = 4;
int startVertex = 0;

bool visited[MAX];
int queue[MAX];
int front = -1, rear = -1;

void enqueue(int value) {
    if (rear == MAX - 1) {
        printf("Queue Overflow\n");
        return;
    }
    if (front == -1) front = 0;
    queue[++rear] = value;
}

int dequeue() {
    if (front == -1 || front > rear) {
        printf("Queue Underflow\n");
        exit(EXIT_FAILURE);
    }
    return queue[front++];
}

void dfs(int vertex) {
    visited[vertex] = true;
    printf("%d ", vertex);

    for (int i = 0; i < numVertices; i++) {
        if (graph[vertex][i] == 1 && !visited[i]) {
            dfs(i);
        }
    }
}

void bfs(int startVertex) {
    for (int i = 0; i < numVertices; i++) visited[i] = false;
    enqueue(startVertex);
    visited[startVertex] = true;

    while (front <= rear) {
        int currentVertex = dequeue();
        printf("%d ", currentVertex);

        for (int i = 0; i < numVertices; i++) {
            if (graph[currentVertex][i] == 1 && !visited[i]) {
                enqueue(i);
                visited[i] = true;
            }
        }
    }
}

int main() {
    printf("Adjacency Matrix:\n");
    for (int i = 0; i < numVertices; i++) {
        for (int j = 0; j < numVertices; j++) {
            printf("%d ", graph[i][j]);
        }
        printf("\n");
    }

    printf("\nDFS Traversal starting from vertex %d:\n", startVertex);
    for (int i = 0; i < numVertices; i++) visited[i] = false;
    dfs(startVertex);

    printf("\n\nBFS Traversal starting from vertex %d:\n", startVertex);
    bfs(startVertex);

    return 0;
}
