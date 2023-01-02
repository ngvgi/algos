class Graph:
    def __init__(self, edges):
        self.edges = edges
        self.graph_dict = {}

        for start, dest in self.edges:
            if start in self.graph_dict:
                self.graph_dict[start].append(dest)
            else:
                self.graph_dict[start] = [dest]
        print("Graph dict: {}".format(self.graph_dict))

    def get_paths(self, start, end, path=[]):
        path = path + [start]

        if start == end:
            return [path]

        if start not in self.graph_dict:
            return []

        paths = []
        for node in self.graph_dict[start]:
            if node not in path:
                new_paths = self.get_paths(node, end, path)
                for p in new_paths:
                    paths.append(p)

        return paths


routes = [
    ('Mumbai', 'Paris'),
    ('Mumbai', 'Dubai'),
    ('Paris', 'Dubai'),
    ('Paris', 'New York'),
    ('Dubai', 'New York'),
    ('New york', 'Toronto')
]

route_path = Graph(routes)

start = 'Mumbai'
end = 'New York'

print('Path between {} and {} is => {}'.format(
    start, end, route_path.get_paths(start, end)))
