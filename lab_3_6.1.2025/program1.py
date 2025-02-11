row = [-1, 1, 0, 0]
col = [0, 0, -1, 1]

def is_valid(grid, x, y, visited):
    return 0 <= x < len(grid) and 0 <= y < len(grid[0]) and grid[x][y] != -1 and not visited[x][y]

def dfs(grid, x, y, end_x, end_y, visited, current_path, current_cost, min_cost, best_path, all_paths):
    if x == end_x and y == end_y:
        all_paths.append(''.join(current_path))
        if current_cost < min_cost[0]:
            min_cost[0] = current_cost
            best_path[0] = ''.join(current_path)
        return
    
    visited[x][y] = True

    for i in range(4):
        new_x, new_y = x + row[i], y + col[i]
        if is_valid(grid, new_x, new_y, visited):
            if i == 0:
                current_path.append('U')
            elif i == 1:
                current_path.append('D')
            elif i == 2:
                current_path.append('L')
            elif i == 3:
                current_path.append('R')
            dfs(grid, new_x, new_y, end_x, end_y, visited, current_path, current_cost + grid[new_x][new_y], min_cost, best_path, all_paths)
            current_path.pop()
    
    visited[x][y] = False

def find_all_paths_with_min_cost(grid, start_x, start_y, end_x, end_y):
    visited = [[False] * len(grid[0]) for _ in range(len(grid))]
    current_path = []
    all_paths = []
    min_cost = [float('inf')]
    best_path = ['']
    
    dfs(grid, start_x, start_y, end_x, end_y, visited, current_path, grid[start_x][start_y], min_cost, best_path, all_paths)
    
    return all_paths, min_cost[0], best_path[0]

grid = [
    [1, 2, 1, 1],
    [2, -1, 0, 1],
    [3, 1, 1, 1],
    [4, 1, 1, 1]
]

start_x, start_y = 0, 0
end_x, end_y = 3, 2

all_paths, min_cost, best_path = find_all_paths_with_min_cost(grid, start_x, start_y, end_x, end_y)

print(f"Total paths found: {len(all_paths)}")
for i, path in enumerate(all_paths):
    print(f"Path {i + 1}: {path}")

print(f"\nMinimum cost to reach the target: {min_cost}")
print(f"Path with minimum cost: {best_path}")
