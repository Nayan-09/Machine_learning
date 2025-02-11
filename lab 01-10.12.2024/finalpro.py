from collections import deque

def bfs(maze, start, end):
    rows, cols = len(maze), len(maze[0])
    queue = deque([(start, [start])])
    visited = set([start])
    nodes_explored = 0
    
    while queue:
        (x, y), path = queue.popleft()
        nodes_explored += 1
        
        if (x, y) == end:
            return path, nodes_explored
        
        for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < rows and 0 <= ny < cols and maze[nx][ny] == 1 and (nx, ny) not in visited:
                visited.add((nx, ny))
                queue.append(((nx, ny), path + [(nx, ny)]))
    
    return None, nodes_explored

def dfs(maze, start, end):
    rows, cols = len(maze), len(maze[0])
    stack = [(start, [start])]
    visited = set([start])
    nodes_explored = 0

    while stack:
        (x, y), path = stack.pop()
        nodes_explored += 1

        if (x, y) == end:
            return path, nodes_explored

        for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < rows and 0 <= ny < cols and maze[nx][ny] == 1 and (nx, ny) not in visited:
                visited.add((nx, ny))
                stack.append(((nx, ny), path + [(nx, ny)]))

    return None, nodes_explored

def print_results(method, path, nodes_explored):
    if path:
        print(f"{method} Path Found: {path}")
    else:
        print(f"{method} No Path Found")
    print(f"Nodes Explored: {nodes_explored}\n")

def main():
    maze = [
        [1, 0, 1, 1, 1, 1],
        [1, 0, 1, 0, 1, 0],
        [1, 1, 1, 0, 1, 1],
        [0, 0, 0, 0, 1, 0],
        [1, 1, 1, 1, 1, 1]
    ]
    start = (0, 0)
    end = (4, 5)
    
    print("Solving maze using BFS and DFS:\n")
    
    # BFS
    bfs_path, bfs_nodes = bfs(maze, start, end)
    print_results("BFS", bfs_path, bfs_nodes)
    
    # DFS
    dfs_path, dfs_nodes = dfs(maze, start, end)
    print_results("DFS", dfs_path, dfs_nodes)

    # Comparison
    print("Comparison of BFS and DFS:")
    print(f"Nodes Explored by BFS: {bfs_nodes}")
    print(f"Nodes Explored by DFS: {dfs_nodes}")

if __name__ == "__main__":
    main()
