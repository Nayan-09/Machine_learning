def dfs(graph, node, visited, parents, target, found):
    """
    Helper DFS function to traverse graph and track parents.
    """
    if node in visited:
        return False
    visited.add(node)

    # Stop if we find the target during traversal
    if node == target:
        found[0] = True
        return True

    for neighbor in graph[node]:
        if neighbor not in visited:
            parents[neighbor] = node  # Track parent for path reconstruction
            if dfs(graph, neighbor, visited, parents, target, found):
                return True
    return False

def bidirectional_dfs_with_path(graph, source, target):
    if source == target:
        return [source]  # Source and target are the same

    # Visited sets
    visited_from_source = set()
    visited_from_target = set()

    # Parent dictionaries
    source_parents = {source: None}
    target_parents = {target: None}

    # Flags to stop when overlap is found
    found = [False]  # Shared mutable flag to indicate stopping condition

    # Start DFS from source and target
    dfs(graph, source, visited_from_source, source_parents, None, found)
    dfs(graph, target, visited_from_target, target_parents, None, found)

    # Check for overlap
    common_nodes = visited_from_source & visited_from_target
    if common_nodes:
        meeting_node = list(common_nodes)[0]  # Pick the first common node
        return reconstruct_path(source_parents, target_parents, meeting_node)

    return None  # No path found

def reconstruct_path(source_parents, target_parents, meeting_node):
    """
    Reconstruct the path from source to target using parent dictionaries.
    """
    path_from_source = []
    current = meeting_node
    while current is not None:
        path_from_source.append(current)
        current = source_parents[current]
    path_from_source.reverse()

    path_from_target = []
    current = meeting_node
    while current is not None:
        current = target_parents[current]
        if current is not None:
            path_from_target.append(current)

    return path_from_source + path_from_target

# Example graph
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D'],
    'C': ['A', 'D'],
    'D': ['B', 'C', 'E'],
    'E': ['D']
}

# Test Bidirectional DFS
path = bidirectional_dfs_with_path(graph, 'A', 'E')
print("Bidirectional DFS Path:", path)
