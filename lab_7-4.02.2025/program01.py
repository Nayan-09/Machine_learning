# implement water jug problem using the concept of DFS 

def water_jug_dfs(x, y, z):
    stack = [(0, 0)]  # Stack for DFS, starting with empty jugs
    visited = set()   # To track visited states

    while stack:
        a, b = stack.pop()  # Get the last added state
        if (a, b) in visited:
            continue
        visited.add((a, b))

        print(f"Current state: ({a}, {b})")  # Print current state

        if a == z or b == z:  # Goal check
            print("Solution found!")
            return True

        # Generate all possible next states
        next_states = set()
        next_states.add((x, b))   # Fill jug 1
        next_states.add((a, y))   # Fill jug 2
        next_states.add((0, b))   # Empty jug 1
        next_states.add((a, 0))   # Empty jug 2
        
        # Pour jug 1 -> jug 2
        pour1_to_2 = min(a, y - b)
        next_states.add((a - pour1_to_2, b + pour1_to_2))
        
        # Pour jug 2 -> jug 1
        pour2_to_1 = min(b, x - a)
        next_states.add((a + pour2_to_1, b - pour2_to_1))

        for state in next_states:
            if state not in visited:
                stack.append(state)  # Push new state to stack

    print("No solution possible.")
    return False

# Example usage
x, y, z = 4, 3, 2  # Jug capacities and target amount
water_jug_dfs(x, y, z)
