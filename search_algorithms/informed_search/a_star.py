import heapq
from core.node import Node
from core.utils import manhattan, get_neighbors, reconstruct_path

def a_star(grid, start, goal):
    open_set = [Node(start, h=manhattan(start, goal))]
    heapq.heapify(open_set)
    visited = {}

    while open_set:
        node = heapq.heappop(open_set)
        if node.position == goal:
            return reconstruct_path(node)
        if node.position in visited and visited[node.position] <= node.g:
            continue
        visited[node.position] = node.g
        for nr, nc, cost in get_neighbors(node.position, grid):
            g_new = node.g + cost
            h_new = manhattan((nr, nc), goal)
            child = Node((nr, nc), g_new, h_new, node)
            heapq.heappush(open_set, child)
    return None
