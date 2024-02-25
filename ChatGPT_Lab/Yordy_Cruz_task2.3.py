def depth_first_search(graph, start, end=None, path=None, visited=None):
    """
    Performs a depth-first search (DFS) in a graph from a start node to an optional end node.

    Args:
    - graph (dict): The graph represented as a dictionary where keys are node labels and values are sets of adjacent nodes.
    - start: The starting node for the DFS.
    - end (optional): The end node for the DFS. If provided, the search stops when the end is reached.
    - path (list, optional): The current path taken to reach the start node. Used internally for recursion.
    - visited (set, optional): The set of nodes that have been visited. Used internally for recursion.

    Returns:
    - list of lists: A list containing all paths from start to end. Each path is represented as a list of nodes.
    """

    # Initialize visited set and path list if not provided
    if visited is None:
        visited = set()
    if path is None:
        path = [start]
    else:
        path += [start]  # Append current start node to the path

    # Check if the current node is the end node
    if start == end:
        return [path]  # Return the current path as the only element in a list

    # Check if the current node was already visited to detect cycles
    if start in visited:
        print(f"Cycle detected at {start}, returning current path.")
        return [path]  # Return current path to avoid infinite recursion

    # Mark the current node as visited
    visited.add(start)

    # Initialize a list to store all paths found
    paths = []

    # Explore all adjacent nodes that haven't been visited
    for next_node in graph[start] - visited:
        # Recursively perform DFS on the next node
        newpaths = depth_first_search(graph, next_node, end, path, visited)
        
        # Append new paths found to the paths list
        for newpath in newpaths:
            paths.append(newpath)

    # Return the list of all paths found
    return paths

# Example usage
graph = {
    'A': {'B', 'C'},
    'B': {'A', 'D', 'E'},
    'C': {'A', 'F'},
    'D': {'B'},
    'E': {'B', 'F'},
    'F': {'C', 'E'}
}
print(depth_first_search(graph, 'A', 'F'))
