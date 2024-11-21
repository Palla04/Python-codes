import heapq

def a_star(graph, heuristic, start, goal):
    # Priority queue to store nodes with their cost (f = g + h)
    open_set = [(0, start)]
    # Store the cost of reaching each node
    g_cost = {node: float('inf') for node in graph}
    g_cost[start] = 0
    # Store the path
    came_from = {}

    while open_set:
        # Get the node with the lowest f value
        _, current = heapq.heappop(open_set)

        if current == goal:
            # Reconstruct the path from start to goal
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            path.append(start)
            print(f"Shortest path: {' -> '.join(reversed(path))}")
            print(f"Total cost: {g_cost[goal]}")
            return

        # Explore neighbors
        for neighbor, weight in graph[current].items():
            tentative_g_cost = g_cost[current] + weight

            if tentative_g_cost < g_cost[neighbor]:
                g_cost[neighbor] = tentative_g_cost
                f_cost = tentative_g_cost + heuristic[neighbor]
                heapq.heappush(open_set, (f_cost, neighbor))
                came_from[neighbor] = current

    print(f"No path found from {start} to {goal}.")

# Input helper function
def get_graph_and_heuristics():
    # Create an empty graph
    graph = {}
    heuristic = {}

    # Number of nodes
    num_nodes = int(input("Enter the number of nodes: "))
    print("Enter the nodes:")
    nodes = [input().strip() for _ in range(num_nodes)]

    for node in nodes:
        graph[node] = {}

    # Number of edges
    num_edges = int(input("Enter the number of edges: "))
    print("Enter the edges (start end cost):")
    for _ in range(num_edges):
        u, v, cost = input().split()
        cost = int(cost)
        graph[u][v] = cost
        graph[v][u] = cost  # For undirected graph; remove this for directed graph

    # Heuristic values
    print("Enter heuristic values for each node (node value):")
    for node in nodes:
        heuristic[node] = int(input(f"{node}: "))

    return graph, heuristic

if __name__ == "__main__":
    # Get the graph and heuristics from the user
    graph, heuristic = get_graph_and_heuristics()

    # Input start and goal nodes
    start = input("Enter the start node: ").strip()
    goal = input("Enter the goal node: ").strip()

    # Run the A* algorithm
    a_star(graph, heuristic, start, goal)
