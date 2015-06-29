class Graph:
    def __init__(self, vertices, edges):
        self.vertices = vertices
        self.edges = edges

    def get_vertices_without_inbound_edges(self):
        have_inbounds = {vertex: False for vertex in self.vertices}
        for edge in self.edges:
            have_inbounds[edge.end_vertex] = True
        return [self.vertices[vertex] for vertex in have_inbounds.keys() if not have_inbounds[vertex]]

    def get_topological_order(self, start_vertices):
        result = []
        stack = []
        stack.extend(start_vertices)
        visited = {vertex: False for vertex in self.vertices}

        while len(stack) > 0:
            current_vertex = stack[-1]

            visited[current_vertex.label] = True
            neighbors = [self.vertices[x]
                         for x in current_vertex.outbound_edges
                         if not visited[x]]

            if len(neighbors) == 0:
                result.append(current_vertex.label)
                stack.pop()

            stack.extend(neighbors)

        return result

    def __str__(self):
        return "VERTICES:\n%s" % '\n'.join([str(vertex) for _, vertex in self.vertices.iteritems()])

class Vertex:
    def __init__(self, label):
        self.label = label
        self.outbound_edges = []  # list of string labels

    def __str__(self):
        return "LABEL: %s, DEPS: %s" % (self.label, ', '.join(self.outbound_edges))


class Edge:
    def __init__(self, start_vertex, end_vertex):
        self.start_vertex = start_vertex
        self.end_vertex = end_vertex

    def __str__(self):
        return "%d -> %d" % (self.start_vertex.label, self.end_vertex.label)
