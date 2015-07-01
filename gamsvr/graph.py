class Graph:
    def __init__(self, vertices, edges):
        self.vertices = vertices
        self.edges = edges

    def dijkstra(self, index):
        start_vertex = self.vertices[index]
        # Initialization: setting all known shortest distances to infinity,
        # and the start vertex will have the shortest distance to itself equal to 0.
        INFINITY = 1e10
        distances = [INFINITY for _ in self.vertices]
        shortest_path_predecessor = [None for _ in self.vertices]
        distances[start_vertex.label] = 0

        # Visiting every vertex in the graph...
        visit_list = [vertex for vertex in self.vertices]

        while len(visit_list) > 0:
            # ...but selecting the vertex with the shortest known distance every time.
            #
            # We can avoid doing the linear-time lookup every time by using a Fibonacci Heap instead,
            # thus reducing the complexity to O(E log V).
            shortest_distance_vertex = visit_list[0]
            shortest_distance_index = 0

            for (index, vertex) in enumerate(visit_list):
                if distances[vertex.label] < distances[shortest_distance_index]:
                    shortest_distance_vertex = vertex
                    shortest_distance_index = index

            visit_list.pop(shortest_distance_index)

            # For each adjacent vertex v, check if the path from the current vertex would be more efficient
            # than the one we've known before. I.e., if distance[current] + weight(current->v) < distance[v].
            for edge in shortest_distance_vertex.outbound_edges:
                alternative_distance = distances[shortest_distance_vertex.label] + edge.weight
                if alternative_distance < distances[edge.end_vertex.label]:
                    # If we have indeed found a better path, remembering the new distance and predecessor.
                    distances[edge.end_vertex.label] = alternative_distance
                    shortest_path_predecessor[edge.end_vertex.label] = shortest_distance_vertex.label

        # We can avoid the shortest_path_predecessor array completely, but we'll return it in case there's
        # a need to output the actual PATH instead of just the shortest distances.
        return distances, shortest_path_predecessor


class Vertex:
    def __init__(self, label):
        self.label = label
        self.outbound_edges = []

    def __str__(self):
        return "Label: %d    Edges: %s" % (self.label, ', '.join([str(edge) for edge in self.outbound_edges]))


class Edge:
    def __init__(self, start_vertex, end_vertex, weight):
        self.start_vertex = start_vertex
        self.end_vertex = end_vertex
        self.weight = weight

    def __str__(self):
        return "%d ---%d---> %d" % (self.start_vertex.label, self.weight, self.end_vertex.label)
