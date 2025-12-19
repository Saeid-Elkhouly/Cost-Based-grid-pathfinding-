from core.node import Node
from core.utlis import manhattan, get_neighbors, reconstruct_path

def hill_climbing(grid, start, goal):
    current = Node(start, h=manhattan(start, goal))
    while True:
        neighbors = get_neighbors(current.position, grid)
        if not neighbors:
            break
        best_neighbor = min(neighbors, key=lambda x: manhattan(x[0], goal))
        best_pos, best_cost = best_neighbor
        best_h = manhattan(best_pos, goal)
        if best_h >= current.h:
            break
        current = Node(best_pos, current.g + best_cost, best_h, current)
        if best_pos == goal:
            break
    return reconstruct_path(current)
