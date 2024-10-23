import heapq

def dijkstra(graph, source, destination, V):
    # Initialize distances with infinity for all vertices except the source
    distances = {i: float('inf') for i in range(V)}
    distances[source] = 0

    # Priority queue to keep track of the shortest distance node
    priority_queue = [(0, source)]  # (distance, vertex)

    # Dictionary to track the shortest path
    path = {i: [] for i in range(V)}
    path[source] = [source]

    while priority_queue:
        # Get the vertex with the smallest distance
        curr_distance, curr_vertex = heapq.heappop(priority_queue)

        if curr_vertex == destination:
            print(f"Shortest distance from {source} to {destination}: {curr_distance}")
            print(f"Path: {' -> '.join(map(str, path[curr_vertex]))}")
            return

        # Explore all adjacent vertices
        for neighbor, weight in graph[curr_vertex].items():
            distance = curr_distance + weight

            # If a shorter path to neighbor is found
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))
                # Update the path to this neighbor
                path[neighbor] = path[curr_vertex] + [neighbor]

    print(f"No path exists from {source} to {destination}.")

# Function to add an edge to the graph
def add_edge(graph, u, v, w):
    graph[u][v] = w
    graph[v][u] = w  # Comment out this line for a directed graph

if __name__ == "__main__":
    # Number of vertices in the graph
    V = int(input("Enter the number of vertices: "))

    # Initialize an empty graph (adjacency list)
    graph = {i: {} for i in range(V)}

    # Number of edges in the graph
    E = int(input("Enter the number of edges: "))

    # Add edges to the graph
    print("Enter the edges (u v w):")
    for _ in range(E):
        u, v, w = map(int, input().split())
        add_edge(graph, u, v, w)

    # Get the source and destination vertices
    source = int(input("Enter the source vertex: "))
    destination = int(input("Enter the destination vertex: "))

    # Perform Dijkstra's algorithm to find the shortest path
    dijkstra(graph, source, destination, V)
