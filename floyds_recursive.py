# Floyd Warshall algroithm using Recursion with Python
No_path = float('inf')
def recursive_floyd(graph, i, j, k):
    """
    Recursive function to find the shortest path between vertices i and j
    via intermediate vertices up to k in a graph represented as an adjacency matrix.
    
    Args:
        graph (list of list): The adjacency matrix of the graph.
        i (int): Source vertex.
        j (int): Destination vertex.
        k (int): Intermediate vertex to consider.
    
    Returns:
        int: The shortest path length between vertices i and j via intermediate vertex k.
    """
    if k == 0:
        return graph[i][j]
    else:
        # Calculate the shortest path without using vertex k
        without_k = recursive_floyd(graph, i, j, k - 1)

        # Calculate the shortest path with vertex k as an intermediate vertex
        with_k = recursive_floyd(graph, i, k, k - 1) + recursive_floyd(graph, k, j, k - 1)

        # Choose the minimum of the two options
        return min(without_k, with_k)

def floyd_recursive_wrapper(graph):
    """
    Wrapper function to initiate the recursive Floyd's algorithm for all pairs of vertices.
    
    Args:
        graph (list of list): The adjacency matrix of the graph.
    
    Returns:
        list of list: The matrix of shortest path lengths between all pairs of vertices.
    """
    num_vertices = len(graph)
    shortest_paths = [[0] * num_vertices for _ in range(num_vertices)]

    for i in range(num_vertices):
        for j in range(num_vertices):
            shortest_paths[i][j] = recursive_floyd(graph, i, j, num_vertices - 1)

    return shortest_paths