class Graph:
    def __init__(self, edges):
        self.edges = edges
        self.graph_path = {}
        for i, j in self.edges:
            if i in self.graph_path:
                self.graph_path[i].append(j)
            else:
                self.graph_path[i] = [j]

        print(self.graph_path)

    def get_all_paths(self, source, destination, path=[]):
        path = path + [source]
        if source == destination:
            return [path]

        if source not in self.graph_path:
            return []

        paths = []
        for node in self.graph_path[source]:
            if node not in paths:
                new_path = self.get_all_paths(node, destination, path)
                for p in new_path:
                    paths.append(p)
        return paths

    def smallest_path(self, source, destination):
        path = self.get_all_paths(source, destination)
        path_length = {}
        for i in path:
            if len(i) not in path_length:
                path_length[len(i)] = [i]
            else:
                path_length[len(i)].append(i)
        short = min(path_length.keys())
        return path_length[short]


if __name__ == "__main__":
    routes = [
        ("Mumbai", "Paris"),
        ("Mumbai", "New York"),
        ("Paris", "Dubai"),
        ("Paris", "Toronto"),
        ("Paris", "Delhi"),
        ("Delhi", "Rwanda"),
        ("Dubai", "New York"),
        ("Delhi", "Kentucky"),
        ("Delhi", "New York"),
        ("Delhi", "Cincinnati Ohio")
    ]

    route_graph = Graph(routes)
    source = "Mumbai"
    destination = "New York"
    print(f"Path from {source} to {destination} is ", route_graph.get_all_paths(source, destination))
    print(route_graph.smallest_path(source, destination))
