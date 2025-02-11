from collections import deque

def bidirectional_bfs_with_path(graph, source, target):
    if source == target:
        return [source]  # Source and target are the same

    # Queues for BFS
    source_queue = deque([source])
    target_queue = deque([target])

    # Parent dictionaries to reconstruct the path
    source_parents = {source: None}
    target_parents = {target: None}

    # Visited dictionaries
    visited_from_source = set([source])
    visited_from_target = set([target])

    # Function to reconstruct path
    def reconstruct_path(meeting_node):
        # Path from source to meeting node
        path_from_source = []
        current = meeting_node
        while current is not None:
            path_from_source.append(current)
            current = source_parents[current]
        path_from_source.reverse()

        # Path from meeting node to target
        path_from_target = []
        current = meeting_node
        while current is not None:
            current = target_parents[current]
            if current is not None:
                path_from_target.append(current)

        # Combine both paths
        return path_from_source + path_from_target

    # Perform BFS
    while source_queue and target_queue:
        # Step from source side
        if source_queue:
            curr_source = source_queue.popleft()
            for neighbor in graph[curr_source]:
                if neighbor not in visited_from_source:
                    source_parents[neighbor] = curr_source
                    visited_from_source.add(neighbor)
                    source_queue.append(neighbor)

                    # Check for overlap
                    if neighbor in visited_from_target:
                        return reconstruct_path(neighbor)

        # Step from target side
        if target_queue:
            curr_target = target_queue.popleft()
            for neighbor in graph[curr_target]:
                if neighbor not in visited_from_target:
                    target_parents[neighbor] = curr_target
                    visited_from_target.add(neighbor)
                    target_queue.append(neighbor)

                    # Check for overlap
                    if neighbor in visited_from_source:
                        return reconstruct_path(neighbor)

    return None  # If no path exists

# Example graph
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D'],
    'C': ['A', 'D'],
    'D': ['B', 'C', 'E'],
    'E': ['D']
}

# Test BFS with path reconstruction
path = bidirectional_bfs_with_path(graph, 'A', 'E')
print("Bidirectional BFS Shortest Path:", path)
