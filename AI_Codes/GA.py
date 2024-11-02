import random

# Configuration
N = 8  # Number of queens and size of the board
POPULATION_SIZE = 100
MAX_GENERATIONS = 1000
MUTATION_RATE = 0.1

# Generate a random individual
def random_individual():
    return [random.randint(0, N - 1) for _ in range(N)]

# Calculate fitness based on non-attacking queen pairs
def fitness(individual):
    non_attacking_pairs = 0
    for i in range(N):
        for j in range(i + 1, N):
            # Check if queens are not in the same row or diagonal
            if individual[i] != individual[j] and abs(individual[i] - individual[j]) != j - i:
                non_attacking_pairs += 1
    return non_attacking_pairs

# Selection function to select individuals based on fitness
def selection(population):
    population = sorted(population, key=lambda ind: -fitness(ind))
    return population[:POPULATION_SIZE // 2]

# Crossover function
def crossover(parent1, parent2):
    crossover_point = random.randint(1, N - 1)
    child1 = parent1[:crossover_point] + parent2[crossover_point:]
    child2 = parent2[:crossover_point] + parent1[crossover_point:]
    return child1, child2

# Mutation function
def mutate(individual):
    if random.random() < MUTATION_RATE:
        mutate_point = random.randint(0, N - 1)
        individual[mutate_point] = random.randint(0, N - 1)
    return individual

# Main genetic algorithm function
def genetic_algorithm():
    # Initialize population
    population = [random_individual() for _ in range(POPULATION_SIZE)]
    
    for generation in range(MAX_GENERATIONS):
        # Check if any solution is optimal (28 non-attacking pairs for 8-queens)
        for individual in population:
            if fitness(individual) == 28:
                print(f"Solution found in generation {generation}:")
                print(individual)
                return individual
        
        # Selection
        selected_population = selection(population)
        
        # Create the next generation
        next_generation = []
        while len(next_generation) < POPULATION_SIZE:
            parent1, parent2 = random.sample(selected_population, 2)
            child1, child2 = crossover(parent1, parent2)
            next_generation.append(mutate(child1))
            next_generation.append(mutate(child2))
        
        population = next_generation
    
    print("No solution found within the maximum number of generations.")
    return None

# Run the algorithm
solution = genetic_algorithm()
if solution:
    # Display the board for the solution
    print("Final board configuration:")
    for row in range(N):
        line = ""
        for col in range(N):
            if solution[col] == row:
                line += "Q "
            else:
                line += ". "
        print(line)
