# main.py
import sys
import os
import time
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
    """Calculate the total cost of a path based on grid cell values."""
    if not path:
        return 0
    
    total_cost = 0
    for row, col in path:
        total_cost += grid[row][col]
    
    return total_cost


def run_test(grid, start, goal, test_name):
    """Run all algorithms and print Path and Cost."""
    
    print("\n" + "="*80)
    print(f"{test_name}")
    print("="*80)
    
    # Display grid
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
        # Run algorithm
        path = algo_func(grid, start, goal)
        
        # Calculate cost
        cost = calculate_path_cost(path, grid) if path else "N/A"
        path_str = str(path) if path else "No Path Found"
        
        # Print simple row
        print(f"{name:<15} {cost:<10} {path_str}")
    
    print("-" * 80)


def main():
    print("\n" + "="*80)
    print("AI SEARCH ALGORITHMS - PATH & COST")
    print("="*80)
    
    # ------------------------
    # Test 1: Uniform cost grid
    # ------------------------
    grid1 = [
        [1, 1, 1, 1],
        [1, 0, 1, 0],
        [1, 1, 1, 1],
    ]
    run_test(grid1, (0, 0), (2, 3), "TEST 1: UNIFORM COST")

    # ------------------------
    # Test 2: Varying cost grid
    # ------------------------
    grid2 = [
        [1, 3, 1, 1],
        [1, 0, 5, 0],
        [2, 1, 1, 1],
    ]
    run_test(grid2, (0, 0), (2, 3), "TEST 2: VARYING COST")

    # ------------------------
    # Test 3: High cost corridor
    # ------------------------
    grid3 = [
        [1, 1, 1, 1, 1, 1],
        [1, 9, 9, 9, 9, 1],
        [1, 1, 1, 1, 1, 1],
        [1, 9, 9, 9, 9, 1],
        [1, 1, 1, 1, 1, 1],
    ]
    run_test(grid3, (0, 0), (4, 5), "TEST 3: HIGH COST CORRIDOR")
    
    print("\nDone.\n")

if __name__ == "__main__":
    main()
