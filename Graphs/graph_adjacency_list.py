# This graph is represented using adjacency list. 
# Flight routes.

class Graph:
    def __init__(self, edges):
        self.edges = edges
        self.graph = {}
        for start, end in self.edges:
            if start in self.graph:
                self.graph[start].append(end)
            else:
                self.graph[start] = [end]

    def get_paths(self, start, end, path=None):
        if path is None:
            path = []
        path = path + [start]

        if start == end:
            return [path]

        if start not in self.graph:
            return []

        paths = []
        for node in self.graph[start]:
            if node not in path:
                new_paths = self.get_paths(node, end, path)
                for p in new_paths:
                    paths.append(p)
        return paths

    def get_shortest_path(self, start, end, path=None):
        if path is None:
            path = []
        path = path + [start]

        if start == end:
            return path

        if start not in self.graph:
            return None

        shortest_path = None
        for node in self.graph[start]:
            if node not in path:
                sp = self.get_shortest_path(node, end, path)
                if sp:
                    if shortest_path is None or len(sp) < len(shortest_path):
                        shortest_path = sp
        return shortest_path


routes_graph = [
    ("Mumbai", "Paris"),
    ("Mumbai", "Dubai"),
    ("Paris", "Dubai"),
    ("Paris", "New York"),
    ("Dubai", "New York"),
    ("New York", "Toronto"),
]

routes_graph = Graph(routes_graph)

print(routes_graph.get_shortest_path('Mumbai', 'Toronto'))
