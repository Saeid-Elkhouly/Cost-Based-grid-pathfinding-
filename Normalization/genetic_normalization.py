
import random
import copy
import numpy as np # type: ignore

# ==================================================
# Genetic Algorithm Based Normalization for Grid Costs
# ==================================================

POPULATION_SIZE = 30
GENERATIONS = 50
MUTATION_RATE = 0.1
CROSSOVER_RATE = 0.8

# --------------------------------------------------
# Helper Functions
# --------------------------------------------------

def flatten_grid(grid):
    return [cell for row in grid for cell in row if cell != -1]

def rebuild_grid(original_grid, normalized_values):
    idx = 0
    new_grid = copy.deepcopy(original_grid)
    for i in range(len(new_grid)):
        for j in range(len(new_grid[0])):
            if new_grid[i][j] != -1:
                new_grid[i][j] = normalized_values[idx]
                idx += 1
    return new_grid

# --------------------------------------------------
# Fitness Function
# --------------------------------------------------

def fitness(individual, data):
    a, b = individual
    normalized = [(a * x + b) for x in data]

    # Penalize values outside [0,1]
    penalty = sum(
        abs(x) for x in normalized if x < 0 or x > 1
    )

    variance = np.var(normalized)
    return variance + penalty * 10

# --------------------------------------------------
# Genetic Operators
# --------------------------------------------------

def selection(population, scores):
    tournament = random.sample(list(zip(population, scores)), 3)
    tournament.sort(key=lambda x: x[1])
    return tournament[0][0]

def crossover(p1, p2):
    if random.random() < CROSSOVER_RATE:
        alpha = random.random()
        return (
            alpha * p1[0] + (1 - alpha) * p2[0],
            alpha * p1[1] + (1 - alpha) * p2[1]
        )
    return p1

def mutation(individual):
    a, b = individual
    if random.random() < MUTATION_RATE:
        a += random.uniform(-0.1, 0.1)
    if random.random() < MUTATION_RATE:
        b += random.uniform(-0.1, 0.1)
    return (a, b)

# --------------------------------------------------
# Main Normalization Function (ENTRY POINT)
# --------------------------------------------------

def normalize_grid_with_genetic_algorithm(grid):
    """
    grid: 2D list
    -1 represents obstacle
    returns: normalized grid
    """

    data = flatten_grid(grid)
    min_val, max_val = min(data), max(data)

    # Initial population
    population = [
        (
            random.uniform(0.5, 1.5) / (max_val - min_val),
            random.uniform(-0.5, 0.5)
        )
        for _ in range(POPULATION_SIZE)
    ]

    for _ in range(GENERATIONS):
        scores = [fitness(ind, data) for ind in population]
        new_population = []

        for _ in range(POPULATION_SIZE):
            parent1 = selection(population, scores)
            parent2 = selection(population, scores)
            child = crossover(parent1, parent2)
            child = mutation(child)
            new_population.append(child)

        population = new_population

    best_individual = min(population, key=lambda ind: fitness(ind, data))
    a, b = best_individual

    normalized_values = [
        max(0, min(1, a * x + b)) for x in data
    ]

    return rebuild_grid(grid, normalized_values)