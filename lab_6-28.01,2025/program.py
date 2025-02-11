import heapq

def manhattan_distance(matrix, goal):
    """Calculate the Manhattan distance heuristic"""
    distance = 0
    for i in range(3):
        for j in range(3):
            if matrix[i][j] == 0:
                continue  # Ignore empty tile
            value = matrix[i][j]
            goal_x, goal_y = [(x, y) for x in range(3) for y in range(3) if goal[x][y] == value][0]
            distance += abs(i - goal_x) + abs(j - goal_y)
    return distance

def get_neighbors(matrix):
    """Generate possible moves (neighbors)"""
    moves = []
    x, y = [(i, j) for i in range(3) for j in range(3) if matrix[i][j] == 0][0]
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # Up, Down, Left, Right
    
    for dx, dy in directions:
        new_x, new_y = x + dx, y + dy
        if 0 <= new_x < 3 and 0 <= new_y < 3:
            new_matrix = [row[:] for row in matrix]
            new_matrix[x][y], new_matrix[new_x][new_y] = new_matrix[new_x][new_y], new_matrix[x][y]
            moves.append(new_matrix)
    
    return moves

def a_star_solver(initial, goal):
    """Solves the 8-puzzle using the A* algorithm"""
    priority_queue = []
    heapq.heappush(priority_queue, (0, initial, [], 0))  # Add cost as a separate element
    visited = set()
    
    while priority_queue:
        cost, current_matrix, path, steps = heapq.heappop(priority_queue)
        if tuple(map(tuple, current_matrix)) in visited:
            continue
        
        visited.add(tuple(map(tuple, current_matrix)))
        
        if current_matrix == goal:
            return path + [current_matrix], steps  # Return the cost (steps)
        
        for neighbor in get_neighbors(current_matrix):
            new_cost = steps + 1 + manhattan_distance(neighbor, goal)
            heapq.heappush(priority_queue, (new_cost, neighbor, path + [current_matrix], steps + 1))
    
    return None, None

def print_solution(path, cost):
    """Prints the solution step by step"""
    for step, state in enumerate(path):
        print(f"Step {step}:")
        for row in state:
            print(row)
        print("\n")
    print(f"Minimum cost to reach the goal: {cost}")

# Initial and Goal Matrices (Solvable Example)
initial_state = [[2, 8, 3], 
                 [1, 6, 4], 
                 [7, 0, 5]]  # '0' represents the empty space

goal_state = [[1, 2, 3], 
              [8, 0, 4], 
              [7, 6, 5]]

solution_path, cost = a_star_solver(initial_state, goal_state)
if solution_path:
    print_solution(solution_path, cost)
else:
    print("No solution found")
