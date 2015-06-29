import graph

def main():
    input_file_path = 'govern.in'
    output_file_path = 'govern.out'

    data = read_data(input_file_path)

    vertices = {}  # use hash instead of list for the ease of using labels
    edges = []
    for labels in data:
        for label in labels:
            if label not in vertices:
                vertices[label] = graph.Vertex(label)

        vertices[labels[0]].outbound_edges.append(labels[1])
        edges.append(graph.Edge(labels[0], labels[1]))

    govern = graph.Graph(vertices, edges)
    last = govern.get_vertices_without_inbound_edges()
    q_order = '\n'.join(x for x in govern.get_topological_order(last))

    write_solution_to_file(output_file_path, q_order)

def read_data(filename):
    with open(filename, 'r') as input_file:
        arr = []
        for line in input_file:
            arr.append(line.rstrip('\n').split())
        return arr


def write_solution_to_file(filename, solution):
    with open(filename, 'w') as output_file:
        output_file.write(str(solution) + '\n')


if __name__ == '__main__':
    main()
