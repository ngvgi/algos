def undirectedPath(edges, nodeA, nodeB):
    graph = create_adj_list(edges)
    return hasPath(graph, nodeA, nodeB, set())


def create_adj_list(edges):
    adj_list = dict()
    for edge in edges:
        for i in range(len(edge)):
            if i < len(edge) - 1:
                adj_list[edge[i]] = adj_list.get(edge[i], []) + [edge[i + 1]]
                continue
            adj_list[edge[i]] = adj_list.get(edge[i], []) + [edge[i-1]]

    return adj_list


def hasPath(graph, src, dst, visited):
    if src == dst:
        return True

    if src in visited:
        return False

    visited.add(src)

    for node in graph[src]:
        if hasPath(graph, node, dst, visited):
            return True

    return False


edges = [
    ['i', 'j'],
    ['k', 'i'],
    ['m', 'k'],
    ['k', 'l'],
    ['o', 'n']
]

print(undirectedPath(edges, 'j', 'm'))
