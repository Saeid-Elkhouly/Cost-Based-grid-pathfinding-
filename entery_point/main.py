# main.py
import sys
import os
import tracemalloc
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


def run_algorithm_with_metrics(algorithm_func, grid, start, goal):
    """
    Run an algorithm and collect evaluation metrics without modifying the algorithm code.
    Returns: dict with path, execution_time, memory_used, and completeness
    """
    # Start memory tracking
    tracemalloc.start()
    
    # Start time tracking
    start_time = time.time()
    
    # Run the algorithm
    path = algorithm_func(grid, start, goal)
    
    # End time tracking
    end_time = time.time()
    execution_time = (end_time - start_time) * 1000  # Convert to milliseconds
    
    # Get memory usage
    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    memory_kb = peak / 1024  # Convert to KB
    
    # Determine completeness
    is_complete = path is not None
    
    return {
        'path': path,
        'execution_time': execution_time,
        'memory_kb': memory_kb,
        'is_complete': is_complete
    }


def find_optimal_cost(grid, start, goal):
    """
    Find the optimal (minimum) path cost by running UCS (guaranteed optimal for positive costs).
    Used to determine if other algorithms found optimal solutions.
    """
    path = ucs(grid, start, goal)
    if path:
        return calculate_path_cost(path, grid)
    return None


def run_test(grid, start, goal, test_name):
    """Run all algorithms on a given grid and display comprehensive evaluation results."""
    
    print("\n" + "="*140)
    print(f"{test_name}")
    print("="*140)
    
    # Display grid
    print("\nGrid Configuration:")
    for i, row in enumerate(grid):
        print(f"  Row {i}: {row}")
    print(f"\n  Start Position: {start}")
    print(f"  Goal Position:  {goal}")
    
    # Define algorithms to test
    algorithms = [
        ("BFS", bfs),
        ("DFS", dfs),
        ("IDS", ids),
        ("UCS", ucs),
        ("A*", a_star),
        ("Hill Climbing", hill_climbing)
    ]
    
    # Find optimal cost for comparison
    optimal_cost = find_optimal_cost(grid, start, goal)
    
    # Run all algorithms and collect metrics
    results = []
    for name, algo_func in algorithms:
        metrics = run_algorithm_with_metrics(algo_func, grid, start, goal)
        
        # Calculate path cost
        path_cost = calculate_path_cost(metrics['path'], grid) if metrics['path'] else None
        
        # Determine optimality
        is_optimal = (path_cost == optimal_cost) if (path_cost is not None and optimal_cost is not None) else False
        
        results.append({
            'name': name,
            'path': metrics['path'],
            'path_cost': path_cost,
            'is_complete': metrics['is_complete'],
            'is_optimal': is_optimal,
            'execution_time': metrics['execution_time'],
            'memory_kb': metrics['memory_kb']
        })
    
    # Print comprehensive results table
    print("\n" + "="*140)
    print("EVALUATION METRICS")
    print("="*140)
    
    # Table header
    header = f"{'Algorithm':<18} {'Complete':<10} {'Optimal':<10} {'Path Cost':<12} {'Time (ms)':<12} {'Memory (KB)':<14} {'Path Length':<12}"
    print(header)
    print("-"*140)
    
    # Table rows
    for result in results:
        name = result['name']
        complete = "✓ Yes" if result['is_complete'] else "✗ No"
        optimal = "✓ Yes" if result['is_optimal'] else "✗ No" if result['is_complete'] else "N/A"
        cost = str(result['path_cost']) if result['path_cost'] is not None else "N/A"
        exec_time = f"{result['execution_time']:.2f}"
        memory = f"{result['memory_kb']:.2f}"
        path_len = str(len(result['path'])) if result['path'] else "N/A"
        
        print(f"{name:<18} {complete:<10} {optimal:<10} {cost:<12} {exec_time:<12} {memory:<14} {path_len:<12}")
    
    # Print detailed paths
    print("\n" + "="*140)
    print("DETAILED PATHS")
    print("="*140)
    
    for result in results:
        print(f"\n{result['name']}:")
        if result['path']:
            print(f"  Path: {result['path']}")
        else:
            print(f"  Path: No solution found")
    
    print("\n" + "="*140 + "\n")


def main():
    print("\n" + "="*140)
    print(" "*45 + "COST-BASED GRID PATHFINDING - ALGORITHM COMPARISON")
    print("="*140)
    
    # ------------------------
    # Test 1: Uniform cost grid (all cells cost 1)
    # ------------------------
    grid1 = [
        [1, 1, 1, 1],
        [1, 0, 1, 0],
        [1, 1, 1, 1],
    ]
    run_test(grid1, (0, 0), (2, 3), "TEST 1: UNIFORM COST GRID (All cells = 1)")

    # ------------------------
    # Test 2: Varying cost grid (shows UCS and A* optimization)
    # ------------------------
    grid2 = [
        [1, 3, 1, 1],
        [1, 0, 5, 0],
        [2, 1, 1, 1],
    ]
    run_test(grid2, (0, 0), (2, 3), "TEST 2: VARYING COST GRID (Different cell costs)")

    # ------------------------
    # Test 3: High cost corridor (forces cost-aware algorithms to find alternate routes)
    # ------------------------
    grid3 = [
        [1, 1, 1, 1, 1, 1],
        [1, 9, 9, 9, 9, 1],
        [1, 1, 1, 1, 1, 1],
        [1, 9, 9, 9, 9, 1],
        [1, 1, 1, 1, 1, 1],
    ]
    run_test(grid3, (0, 0), (4, 5), "TEST 3: HIGH COST CORRIDOR (Expensive middle path)")
    
    print("\n" + "="*140)
    print(" "*55 + "EVALUATION COMPLETE")
    print("="*140 + "\n")

if __name__ == "__main__":
    main()
