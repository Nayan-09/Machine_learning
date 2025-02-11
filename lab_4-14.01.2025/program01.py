import heapq

def uniform_cost_search(graph, start, goal):
   
    pq = [(0, start, [])]  # Priority Queue: (cumulative cost, current node, path)
    visited = set()  # Set to track visited nodes

    while pq:
        cost, node, path = heapq.heappop(pq)

        if node in visited:
            continue
        visited.add(node)

        # Update path
        path = path + [node]

        # Goal check
        if node == goal:
            return cost, path

        # Explore neighbors
        for neighbor, edge_cost in graph[node]:
            if neighbor not in visited:
                heapq.heappush(pq, (cost + edge_cost, neighbor, path))

    return float('inf'), []  # If no path exists


def bfs_unweighted(graph, start, goal):
   
    queue = [(start, [start])]  # Queue: (current node, path)
    visited = set()

    while queue:
        node, path = queue.pop(0)

        if node in visited:
            continue
        visited.add(node)

        # Goal check
        if node == goal:
            return path

        # Explore neighbors
        for neighbor in graph[node]:
            if neighbor not in visited:
                queue.append((neighbor, path + [neighbor]))

    return []  # If no path exists


# Weighted Graph Representation (Adjacency List)
weighted_graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('A', 1), ('D', 2)],
    'C': [('A', 4), ('D', 3)],
    'D': [('B', 2), ('C', 3), ('E', 1)],
    'E': [('D', 1)]
}

# Unweighted Graph Representation for BFS
unweighted_graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D'],
    'C': ['A', 'D'],
    'D': ['B', 'C', 'E'],
    'E': ['D']
}

# Find paths
ucs_cost, ucs_path = uniform_cost_search(weighted_graph, 'A', 'E')
bfs_path = bfs_unweighted(unweighted_graph, 'A', 'E')

# Display Results
print(f"Uniform Cost Search: Cost = {ucs_cost}, Path = {ucs_path}")
print(f"BFS (Unweighted): Path = {bfs_path}")
