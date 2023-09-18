import timeit
import floyds_imperative
import floyds_recursive

NO_PATH = float('inf')
graph = [
        [0, 7, NO_PATH, 8],
        [NO_PATH, 0, 5, NO_PATH],
        [NO_PATH, NO_PATH, 0, 2],
        [NO_PATH, NO_PATH, NO_PATH, 0],
    ]

# Time the recursive Floyd-Warshall
recursive_time = timeit.timeit(lambda: floyds_recursive.floyd(graph), number=100)

# Time the iterative Floyd-Warshall
imperative_time = timeit.timeit(lambda: floyds_imperative.floyd(graph), number=100)

print(f"Recursive Floyd-Warshall took {recursive_time:.6f} seconds.")
print(f"Iterative Floyd-Warshall took {imperative_time:.6f} seconds.")
