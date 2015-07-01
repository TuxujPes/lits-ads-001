from graph import Graph, Vertex, Edge

def main():
    input_file_path = 'gamsvr.in'
    output_file_path = 'gamsvr.out'

    graph, clients, routers = read_graph_from_file(input_file_path)
    highest_optimal_lat = get_highest_optimal_latency(graph, clients, routers)

    write_solution_to_file(output_file_path, highest_optimal_lat)


def get_highest_optimal_latency(graph, clients, routers):
    shortest_pathes = []
    # matrix of paths from routers to clients
    for router_id in routers:
        router_id -= 1
        paths, predecessors = graph.dijkstra(router_id)
        shortest_pathes.append(paths)

    # make list of paths without routers
    paths_to_clients = []
    for shortest_path_per_router in shortest_pathes:
        paths_to_clients_per_router = []
        for client_id in clients:
            paths_to_clients_per_router.append(shortest_path_per_router[client_id-1])
        paths_to_clients.append(paths_to_clients_per_router)

    # get minimal among maximums
    highest_optimal_latency = min([max(x) for x in paths_to_clients])
    return highest_optimal_latency

def read_graph_from_file(filename):
    with open(filename, 'r') as input_file:
        vertex_count, edge_count = [int(x) for x in input_file.readline().split()]
        clients = [int(x) for x in input_file.readline().split()]
        all_machines = []

        vertices = [Vertex(index) for index in range(0, vertex_count)]
        edges = []

        for i in range(0, edge_count):
            start, end, weight = [int(x) for x in input_file.readline().split()]
            start -= 1
            end -= 1
            # Adding the edge to the list of outbound edges for the start vertex.
            edge = Edge(vertices[start], vertices[end], weight)
            vertices[start].outbound_edges.append(edge)

            # For non-directed graphs, an outbound edge is also an inbound one (0 -> 1 == 1 -> 0).
            # Therefore, we reverse the edge and add it to the other vertex.
            reverse_edge = Edge(vertices[end], vertices[start], weight)
            vertices[end].outbound_edges.append(reverse_edge)

            edges.append(edge)
            edges.append(reverse_edge)

            if start+1 not in all_machines:
                all_machines.append(start+1)
            if end+1 not in all_machines:
                all_machines.append(end+1)

        routers = [x for x in all_machines if x not in clients]
        return Graph(vertices, edges), clients, routers


def write_solution_to_file(filename, solution):
    with open(filename, 'w') as output_file:
        output_file.write(str(solution))


if __name__ == '__main__':
    main()
