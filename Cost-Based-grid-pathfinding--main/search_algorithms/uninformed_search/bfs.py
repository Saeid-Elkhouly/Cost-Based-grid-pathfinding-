from collections import deque
from core.node import Node
from core.utlis import get_neighbors, reconstruct_path


def bfs(grid, start, goal):
    """
    Breadth-First Search algorithm.
    
    Returns:
        path (list): list of positions from start to goal
        or None if no path is found
    """

    start_node = Node(start)
    queue = deque([start_node])
    visited = set([start])

    while queue:
        current = queue.popleft()

        
        if current.position == goal:
            return reconstruct_path(current)

        for neighbor_pos, cost in get_neighbors(current.position, grid):
            if neighbor_pos not in visited:
                visited.add(neighbor_pos)
                child = Node(
                    position=neighbor_pos,
                    parent=current
                )
                queue.append(child)

    return None
