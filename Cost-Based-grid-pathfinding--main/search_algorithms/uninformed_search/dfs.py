from core.node import Node
from core.utlis import get_neighbors, reconstruct_path


def dfs(grid, start, goal):
    """
    Depth-First Search algorithm.

    Returns:
        path (list): list of positions from start to goal
        or None if no path is found
    """

    start_node = Node(start)
    stack = [start_node]
    visited = set([start])

    while stack:
        current = stack.pop()

        # goal test
        if current.position == goal:
            return reconstruct_path(current)

        for neighbor_pos, cost in get_neighbors(current.position, grid):
            if neighbor_pos not in visited:
                visited.add(neighbor_pos)
                child = Node(
                    position=neighbor_pos,
                    parent=current
                )
                stack.append(child)

    return None
