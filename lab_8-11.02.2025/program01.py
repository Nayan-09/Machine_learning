# Genetic Algorithm 

# Create a set of Population of 4 string ( 1 to 31) apply roulet wheel for selection method to choose the best
# storing using fitness function f(x) = X^2 - x + 1 these function is maximization funtion in crossover a
# single point crossover is applied on resultent function string . Perform mutation and check the 
# fitness function value at the end


import random

# Fitness function
def fitness(x):
    return x**2 - x + 1  # Given maximization function

# Convert decimal to 5-bit binary string
def to_binary(x):
    return format(x, '05b')

# Convert binary to decimal
def to_decimal(b):
    return int(b, 2)

# Roulette Wheel Selection
def roulette_wheel_selection(population, fitness_values):
    total_fitness = sum(fitness_values)
    selection_probs = [f / total_fitness for f in fitness_values]

    selected = random.choices(population, weights=selection_probs, k=2)
    return selected

# Single-point Crossover
def crossover(parent1, parent2):
    crossover_point = random.randint(1, 4)  # Choose a random point (1 to 4)
    child1 = parent1[:crossover_point] + parent2[crossover_point:]
    child2 = parent2[:crossover_point] + parent1[crossover_point:]
    return child1, child2

# Mutation (Random Bit Flip)
def mutate(binary_str):
    index = random.randint(0, 4)  # Choose a random bit to flip
    mutated_list = list(binary_str)
    mutated_list[index] = '1' if mutated_list[index] == '0' else '0'
    return ''.join(mutated_list)

# Genetic Algorithm Execution
def genetic_algorithm():
    # Step 1: Initialize Population
    population = [random.randint(1, 31) for _ in range(4)]
    print(f"Initial Population (Decimal): {population}")

    # Step 2: Calculate Fitness
    fitness_values = [fitness(x) for x in population]
    print(f"Fitness Values: {fitness_values}")

    # Convert to binary
    binary_population = [to_binary(x) for x in population]
    print(f"Binary Population: {binary_population}")

    # Step 3: Selection using Roulette Wheel
    selected_parents = roulette_wheel_selection(population, fitness_values)
    print(f"Selected Parents: {selected_parents}")

    # Convert selected parents to binary
    parent1, parent2 = map(to_binary, selected_parents)

    # Step 4: Apply Crossover
    child1_bin, child2_bin = crossover(parent1, parent2)
    print(f"Crossover Result: {child1_bin}, {child2_bin}")

    # Step 5: Mutation
    child1_bin = mutate(child1_bin)
    child2_bin = mutate(child2_bin)
    print(f"After Mutation: {child1_bin}, {child2_bin}")

    # Convert children back to decimal
    child1, child2 = to_decimal(child1_bin), to_decimal(child2_bin)
    print(f"New Offspring (Decimal): {child1}, {child2}")

    # Step 6: New Fitness Calculation
    new_fitness_values = [fitness(child1), fitness(child2)]
    print(f"New Fitness Values: {new_fitness_values}")

# Run the Genetic Algorithm
genetic_algorithm()
