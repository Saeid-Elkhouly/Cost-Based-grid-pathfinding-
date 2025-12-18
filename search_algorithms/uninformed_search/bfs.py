from collections import deque
from core.node import Node
from core.utlis import get_neighbors, reconstruct_path


def bfs(grid, start, goal):
    

    start_node = Node(start)
    queue = deque([start_node])

    visited = set()
    visited.add(start)

    while queue:
        current_node = queue.popleft()
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
                queue.append(neighbor_node)

    return None 
