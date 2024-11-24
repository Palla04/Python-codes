import heapq

def a_star(graph, heuristic, s, d):
    # Initialize distances to infinity
    distance = {vertex: float('inf') for vertex in graph}
    distance[s] = 0

    # Priority queue to store (f_cost, vertex)
    priority_queue = [(0, s)]
    path = {vertex: [] for vertex in graph}
    path[s] = [s]

    while priority_queue:
        current_f_cost, curr_ver = heapq.heappop(priority_queue)

        if curr_ver == d:
            print(f"Shortest path between {s} & {d} is {distance[d]}")
            print(f"Path: {path[curr_ver]}")
            return

        for neig, weight in graph[curr_ver].items():
            g_cost = distance[curr_ver] + weight  # Actual cost to neighbor
            if g_cost < distance[neig]:
                distance[neig] = g_cost
                f_cost = g_cost + heuristic[neig]  # Total cost (f = g + h)
                heapq.heappush(priority_queue, (f_cost, neig))
                path[neig] = path[curr_ver] + [neig]

    print(f"No path exists from {s} to {d}.")

if __name__ == "__main__":
    n = int(input("Enter the number of vertices: "))
    e = int(input("Enter the number of edges: "))

    graph = {}
    for _ in range(e):
        u, v, w = map(int, input("Enter the edge (u v w): ").split())
        if u not in graph:
            graph[u] = {}
        if v not in graph:
            graph[v] = {}

        graph[u][v] = w
        graph[v][u] = w  # Remove this for directed graphs

    # Input heuristic values
    heuristic = {}
    print("Enter heuristic values for each vertex:")
    for i in range(n):
        heuristic[i] = int(input(f"Vertex {i}: "))

    source = int(input("Enter the source vertex: "))
    des = int(input("Enter the destination vertex: "))

    a_star(graph, heuristic, source, des)
