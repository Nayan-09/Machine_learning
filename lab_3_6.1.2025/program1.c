#include <stdio.h>
#include <stdlib.h>
#include <limits.h>
#include <string.h>

#define N 4  // Grid size (N x N)
#define MAX_PATHS 1000  // Maximum number of paths to store (for demonstration)

// Directions for moving up, down, left, right
int row[] = {-1, 1, 0, 0};
int col[] = {0, 0, -1, 1};

// Function to check if a position is valid
int is_valid(int grid[N][N], int x, int y, int visited[N][N]) {
    return (x >= 0 && x < N && y >= 0 && y < N && grid[x][y] != -1 && !visited[x][y]);
}

// DFS function to find all paths from (x, y) to (end_x, end_y), calculating the cost
void dfs(int grid[N][N], int x, int y, int end_x, int end_y, int visited[N][N], 
         char path[], int path_index, int current_cost, int *min_cost, 
         char best_path[], int *path_count, char all_paths[MAX_PATHS][N * N], int *all_paths_count) {
    // If we reach the target cell, store the current path and check the cost
    if (x == end_x && y == end_y) {
        // Store the path in all_paths
        strncpy(all_paths[*all_paths_count], path, path_index);
        all_paths[*all_paths_count][path_index] = '\0';  // Null-terminate the string
        (*all_paths_count)++;

        // If the current cost is less than the minimum cost, update min_cost and best_path
        if (current_cost < *min_cost) {
            *min_cost = current_cost;
            strncpy(best_path, path, path_index);  // Store the best path
            best_path[path_index] = '\0';  // Null-terminate the string
        }
        return;
    }

    // Mark the current cell as visited
    visited[x][y] = 1;

    // Explore all 4 possible directions
    for (int i = 0; i < 4; i++) {
        int new_x = x + row[i];
        int new_y = y + col[i];

        // If the move is valid, explore it
        if (is_valid(grid, new_x, new_y, visited)) {
            // Append direction to path
            if (i == 0) path[path_index] = 'U';  // Up
            else if (i == 1) path[path_index] = 'D';  // Down
            else if (i == 2) path[path_index] = 'L';  // Left
            else if (i == 3) path[path_index] = 'R';  // Right

            // Recur to the next cell with the updated cost
            dfs(grid, new_x, new_y, end_x, end_y, visited, path, path_index + 1, 
                 current_cost + grid[new_x][new_y], min_cost, best_path, path_count, all_paths, all_paths_count);
        }
    }

    // Backtrack: unmark the current cell as visited
    visited[x][y] = 0;
}

int main() {
    // Grid: the value of each cell represents the cost of moving through that cell
    // For example, grid[i][j] could represent the cost to move into grid[i][j]
    int grid[N][N] = {
        {1, 2, 1, 1},
        {2, -1, 0, 1},
        {3, 1, 1, 1},
        {4, 1, 1, 1}
    };

    // Start position and end (target) position
    int start_x = 0, start_y = 0;
    int end_x = 3, end_y = 3;

    // Visited array to mark visited cells
    int visited[N][N] = {0};
    char path[N * N];  // Array to store the current path
    int path_index = 0;
    
    // Variables to store the minimum cost and the corresponding path
    int min_cost = INT_MAX;
    char best_path[N * N];  // To store the path with the minimum cost

    // Arrays to store all paths
    char all_paths[MAX_PATHS][N * N];  // To store each valid path
    int all_paths_count = 0;  // Counter to track how many paths have been stored

    // Start the DFS search to find all paths and the minimum cost path
    dfs(grid, start_x, start_y, end_x, end_y, visited, path, path_index, 
         grid[start_x][start_y], &min_cost, best_path, &all_paths_count, all_paths, &all_paths_count);

    // Print all found paths
    printf("Total paths found: %d\n", all_paths_count);
    for (int i = 0; i < all_paths_count; i++) {
        printf("Path %d: %s\n", i + 1, all_paths[i]);
    }

    // Print the minimum cost and the corresponding path
    printf("\nMinimum cost to reach the target: %d\n", min_cost);
    printf("Path with minimum cost: %s\n", best_path);

    return 0;
}
