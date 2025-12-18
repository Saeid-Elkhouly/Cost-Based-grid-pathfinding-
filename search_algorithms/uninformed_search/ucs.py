import heapq
from core.node import Node
from core.utils import get_neighbors, reconstruct_path


def ucs(grid, start, goal):

    start_node = Node(start, g=0, h=0)
    open_list = []
    heapq.heappush(open_list, start_node)
    
    visited = {}
    visited[start] = 0
    
    while open_list:
        current = heapq.heappop(open_list)
        
        if current.position == goal:
            return reconstruct_path(current)
        
        if current.position in visited and visited[current.position] < current.g:
            continue
        
        for neighbor_pos, cost in get_neighbors(current.position, grid):
            new_g = current.g + cost
            
            if neighbor_pos not in visited or new_g < visited[neighbor_pos]:
                visited[neighbor_pos] = new_g
                neighbor_node = Node(neighbor_pos, g=new_g, h=0, parent=current)
                heapq.heappush(open_list, neighbor_node)
    
    return None
