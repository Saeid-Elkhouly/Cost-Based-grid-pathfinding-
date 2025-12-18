from core.node import Node
from core.utlis import get_neighbors, reconstruct_path


def dfs(grid, start, goal):
   

    start_node = Node(start)
    stack = [start_node]

    visited = set()
    visited.add(start)

    while stack:
        current_node = stack.pop()
        current_pos = current_node.position

        if current_pos == goal:
            return reconstruct_path(current_node)

        for neighbor_pos, _ in get_neighbors(current_pos, grid):
            if neighbor_pos not in visited:
                visited.add(neighbor_pos)
                neighbor_node = Node(
                    position=neighbor_pos,
                    parent=current_node
                )
                stack.append(neighbor_node)

    return None
