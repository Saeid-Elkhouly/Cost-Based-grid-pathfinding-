from core.node import Node
from core.utlis import get_neighbors, reconstruct_path


def ids(grid, start, goal):
    
    def depth_limited_search(limit):
        
        def dls_recursive(node, depth):

            if node.position == goal:
                return node
            
            if depth <= 0:
                return None
            
            for neighbor_pos, _ in get_neighbors(node.position, grid):
                child = Node(neighbor_pos, parent=node)
                result = dls_recursive(child, depth - 1)
                if result is not None:
                    return result
            
            return None
        
        start_node = Node(start)
        return dls_recursive(start_node, limit)
    
    max_depth = 100  

    for depth in range(max_depth + 1):
        result = depth_limited_search(depth)
        
        if result is not None:
            return reconstruct_path(result)
    
    return None
