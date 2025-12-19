# main.py
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


from core.node import Node
from core.utlis import is_valid, directions

from search_algorithms.uninformed_search.bfs import bfs
from search_algorithms.uninformed_search.dfs import dfs
from search_algorithms.uninformed_search.ids import ids
from search_algorithms.uninformed_search.ucs import ucs

from search_algorithms.informed_search.a_star import a_star
from search_algorithms.informed_search.hill_climbing import hill_climbing

from visualization.visualizer import visualize_grid

def main():
    # ------------------------
    # 1. Grid setup
    # ------------------------
    grid = [
        [1, 1, 1, 1],
        [1, 0, 1, 0],
        [1, 1, 1, 1],
    ]
    start = (0, 0)
    goal = (2, 3)

    # ------------------------
    # 2. Run uninformed searches
    # ------------------------
    path_bfs = bfs(grid, start, goal)
    path_dfs = dfs(grid, start, goal)
    path_ids = ids(grid, start, goal)
    path_ucs = ucs(grid, start, goal)

    # ------------------------
    # 3. Run informed searches
    # ------------------------
    path_a_star = a_star(grid, start, goal)
    path_hill = hill_climbing(grid, start, goal)

    # ------------------------
    # 4. Print results
    # ------------------------
    print("BFS path:", path_bfs)
    print("DFS path:", path_dfs)
    print("IDS path:", path_ids)
    print("UCS path:", path_ucs)
    print("A* path:", path_a_star)
    print("Hill Climbing path:", path_hill)

    # ------------------------
    # 5. Visualize results
    # ------------------------
    algorithms = [
        ("BFS", path_bfs),
        ("DFS", path_dfs),
        ("IDS", path_ids),
        ("UCS", path_ucs),
        ("A*", path_a_star),
        ("Hill Climbing", path_hill)
    ]

    for name, path in algorithms:
        if path:
            print(f"Visualizing {name} path...")
            visualize_grid(grid, path)
        else:
            print(f"No path found for {name}.")

if __name__ == "__main__":
    main()
