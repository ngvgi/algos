def connectedComponents(graph):
    count = 0
    visited = set()
    for node in graph:
        if explore(graph, node, visited):
            count += 1

    return count


def explore(graph, curr, visited):
    if curr in visited:
        return False

    visited.add(curr)

    for node in graph[curr]:
        explore(graph, node, visited)

    return True


graph = {
    1: [2],
    2: [1, 8],
    6: [7],
    9: [8],
    7: [6, 8],
    8: [9, 7, 2]
}

print(connectedComponents(graph))
