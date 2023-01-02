def dfs(graph, start):
    stack = []
    stack.append(start)

    while len(stack) > 0:
        curr = stack.pop()
        print(curr)
        for node in graph[curr]:
            stack.append(node)


def bfs(graph, start):
    print('\n\n\n BFS:\n')
    queue = []
    queue.append(start)
    while len(queue) > 0:
        curr = queue.pop(0)
        print(curr)
        for node in graph[curr]:
            queue.append(node)


def dfs_recurs(graph, start):
    print(start)
    for node in graph[start]:
        dfs_recurs(graph, node)


def hasPath_DFS(graph, src, dst):
    if src == dst:
        return True

    stack = []
    stack.append(src)
    while len(stack) > 0:
        curr = stack.pop()
        for node in graph[curr]:
            if node == dst:
                return True
            stack.append(node)
    return False


def hasPath_recurr(graph, src, dst):
    if src == dst:
        return True

    for node in graph[src]:
        if hasPath_recurr(graph, node, dst):  # this part is important!
            return True

    return False


def hasPath_BFS(graph, src, dst):
    if src == dst:
        return True

    queue = []
    queue.append(src)

    while len(queue) > 0:
        curr = queue.pop(0)
        if curr == dst:
            return True
        for node in graph[curr]:
            queue.append(node)

    return False


graph = {
    'a': ['c', 'b'],
    'b': ['d'],
    'c': ['e'],
    'd': ['f'],
    'e': [],
    'f': [],
}

""" graph_2 = {
    'a': ['b', 'c'],
    'b': ['d'],
    'c': ['e'],
    'd': ['f'],
    'e': [],
    'f': [],
}
dfs(graph, 'a')
bfs(graph, 'a')
print('\n\n\n DFS recursion:\n')
dfs_recurs(graph_2, 'a') """

print(hasPath_recurr(graph, 'd', 'a'))
