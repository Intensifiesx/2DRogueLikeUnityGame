# Original: dept_first_search
def depth_first_search(graph, start, end=None, path=None, visited=None):

    if visited is None:
        visited = set()
    if path is None:
        path = [start]
    else:
        path = path + [start]

    if start == end:
        return [path]
    if start in visited:
        print(f"Cycle detected at {start}, returning current path.")
        return [path]
    
    visited.add(start)
    paths = []
    for next_node in graph[start] - visited:
        newpaths = depth_first_search(graph, next_node, end, path, visited)
        for newpath in newpaths:
            paths.append(newpath)
    return paths

# main example
graph = {
    'A': {'B', 'C'},
    'B': {'A', 'D', 'E'},
    'C': {'A', 'F'},
    'D': {'B'},
    'E': {'B', 'F'},
    'F': {'C', 'E'}
}
print(depth_first_search(graph, 'A', 'F'))
