# main.py
import sys
import os
import time
from multiprocessing import Process, Queue

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from core.node import Node
from core.utlis import is_valid, directions

from search_algorithms.uninformed_search.bfs import bfs
from search_algorithms.uninformed_search.dfs import dfs
from search_algorithms.uninformed_search.ids import ids
from search_algorithms.uninformed_search.ucs import ucs

from search_algorithms.informed_search.a_star import a_star
from search_algorithms.informed_search.hill_climbing import hill_climbing


def calculate_path_cost(path, grid):
    if not path:
        return 0
    return sum(grid[row][col] for row, col in path)


def run_algo_with_timeout(algo_func, grid, start, goal, timeout=10):
    def target(q):
        try:
            path = algo_func(grid, start, goal)
            q.put(path)
        except Exception as e:
            q.put(f"ERROR: {e}")

    q = Queue()
    p = Process(target=target, args=(q,))
    p.start()
    p.join(timeout)

    if p.is_alive():
        p.terminate()
        p.join()
        return "TIMEOUT"

    result = q.get()
    return result


def run_test(grid, start, goal, test_name):
    print("\n" + "=" * 80)
    print(test_name)
    print("=" * 80)

    print("\nGrid:")
    for row in grid:
        print(f"  {row}")
    print(f"  Start: {start}")
    print(f"  Goal:  {goal}\n")

    algorithms = [
        ("BFS", bfs),
        ("DFS", dfs),
        ("IDS", ids),
        ("UCS", ucs),
        ("A*", a_star),
        ("Hill Climbing", hill_climbing)
    ]

    print("-" * 80)
    print(f"{'Algorithm':<15} {'Cost':<10} {'Path'}")
    print("-" * 80)

    for name, algo_func in algorithms:
        start_time = time.time()
        path = run_algo_with_timeout(algo_func, grid, start, goal, timeout=10)
        elapsed = time.time() - start_time

        if path == "TIMEOUT":
            print(f"{name:<15} TIMEOUT")
            continue
        if isinstance(path, str) and path.startswith("ERROR"):
            print(f"{name:<15} {path}")
            continue

        cost = calculate_path_cost(path, grid) if path else "N/A"
        path_str = str(path) if path else "No Path Found"
        print(f"{name:<15} {cost:<10} {path_str}")

    print("-" * 80)


def main():
    print("\n" + "=" * 80)
    print("AI SEARCH ALGORITHMS - PATH & COST")
    print("=" * 80)

    # ------------------------
    # Grid 20x20 examples
    # ------------------------
    grid1 = [[1] * 20 for _ in range(20)]
    run_test(grid1, (0, 0), (19, 19), "TEST 1: UNIFORM COST 20x20")

    grid2 = [
        [1, 2, 1, 3, 1, 1, 2, 1, 1, 3, 1, 1, 2, 1, 1, 3, 1, 1, 2, 1],
        [1, 0, 0, 0, 1, 2, 0, 0, 1, 0, 1, 2, 0, 0, 1, 0, 1, 2, 0, 1],
        [1, 1, 2, 1, 1, 1, 2, 1, 1, 1, 2, 1, 1, 1, 2, 1, 1, 1, 2, 1],
    ] * 7
    grid2 = grid2[:20]
    run_test(grid2, (0, 0), (19, 19), "TEST 2: VARYING COST 20x20")

    grid3 = [
        [1] * 20,
        [1, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 1],
        [1] * 20,
        [1, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 1],
        [1] * 20,
    ] * 4
    grid3 = grid3[:20]
    run_test(grid3, (0, 0), (19, 19), "TEST 3: HIGH COST CORRIDOR 20x20")

    # ------------------------
    # Small grid 11x11 for all algorithms
    # ------------------------
    small_grid = [[1]*11 for _ in range(11)]
    # نقدر نضيف بعض العقبات لتجربة الخوارزميات
    small_grid[1][2] = 0
    small_grid[2][5] = 0
    small_grid[4][4] = 0
    run_test(small_grid, (0, 0), (10, 10), "SMALL TEST 11x11 (All Algorithms)")

    print("\nDone.\n")


if __name__ == "__main__":
    main()
