import itertools

NO_PATH = float('inf')
graph = [[0, 7, NO_PATH, 8],
         [NO_PATH, 0, 5, NO_PATH],
         [NO_PATH, NO_PATH, 0, 2],
         [NO_PATH, NO_PATH, NO_PATH, 0]]
MAX_LENGTH = len(graph[0])


# New function calculating the shortest path using a recursive function
def shortestpath(start, end, intermediate, distance):
    """
    An implementation of Floyd's algorithm using recursion
    """
    # Calculates the direct paths and exits the recursion only when all intermediate nodes have been tried
    if intermediate == 0:
        return(distance[start][end])

    # Return the minimum between two paths with a different intermediate end
    # node, shortest path between the start point and the intermediate point,
    # plus the intermediate point and the end point
    return min(shortestpath(start, end, intermediate - 1, distance),
               shortestpath(start, intermediate, intermediate - 1, distance) +
               shortestpath(intermediate, end, intermediate - 1, distance))


def floyd(distance):

    # Calculate the node/path combinations
    for start_node, end_node in itertools.product(range(MAX_LENGTH),
                                                  range(MAX_LENGTH)):

        # Assumes that if start_node and end_node are the same
        # then the distance would be zero
        if start_node == end_node:
            distance[start_node][end_node] = 0
            continue

        # Runs the shortest path to calculate the shortest path between
        # start node and end node
        distance[start_node][end_node] = shortestpath(start_node,
                                                      end_node,
                                                      MAX_LENGTH - 1, distance)
    # Output of the function
    return distance

if __name__ == '__main__':
    # Calls the function floyd and passes the definition of graph
    print(floyd(graph))
