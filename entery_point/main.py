import sys
import os


sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from search_algorithms.uninformed_search.bfs import bfs
from search_algorithms.uninformed_search.dfs import dfs


if __name__ == "__main__":

    grid = [
        [1, 1, 1, 1],
        [1, 0, 1, 0],
        [1, 1, 1, 1],
        [0, 1, 1, 1]
    ]

    start = (0, 0)
    goal = (2, 3)

   
    bfs_path = bfs(grid, start, goal)
    if bfs_path:
        print("BFS Path Found:")
        print(bfs_path)
        print("BFS Path length:", len(bfs_path) - 1)
    else:
        print("BFS: No path found")

    print("---------------------------------------")

    
    dfs_path = dfs(grid, start, goal)
    if dfs_path:
        print("DFS Path Found:")
        print(dfs_path)
        print("DFS Path length:", len(dfs_path) - 1)
    else:
        print("DFS: No path found")
