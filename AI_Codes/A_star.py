from queue import PriorityQueue

def a_star_algorithm(graph, start, goal, h):
    """
    Implements the A* algorithm to find the shortest path in a graph.

    Parameters:
    - graph: A dictionary where keys are node names, and values are dictionaries of neighboring nodes and edge costs.
    - start: The starting node.
    - goal: The goal node.
    - h: A heuristic function that estimates the cost from a node to the goal.

    Returns:
    - path: A list of nodes representing the shortest path from start to goal.
    - total_cost: The total cost of the shortest path.
    """
    open_list = PriorityQueue()  # Priority queue for the nodes to be explored
    open_list.put((0, start))  # (priority, node)
    came_from = {start: None}  # To store the best path
    g_score = {start: 0}  # Actual cost from the start node to the current node

    while not open_list.empty():
        current_priority, current_node = open_list.get()

        if current_node == goal:
            path = []
            while current_node is not None:
                path.append(current_node)
                current_node = came_from[current_node]
            return path[::-1], g_score[goal]  # Return the path and total cost

        for neighbor, cost in graph[current_node].items():
            tentative_g_score = g_score[current_node] + cost

            if neighbor not in g_score or tentative_g_score < g_score[neighbor]:
                came_from[neighbor] = current_node
                g_score[neighbor] = tentative_g_score
                f_score = tentative_g_score + h(neighbor, goal)
                open_list.put((f_score, neighbor))

    return None, float('inf')  # Return None and infinite cost if there is no path

def heuristic(node, goal):
    # Assuming a simple heuristic function here. Modify based on the specific problem.
    return 0

def get_graph_input():
    """
    Gets user input to create a graph representation.
    
    Returns:
    - graph: A dictionary representing the graph.
    """
    graph = {}
    print("Enter the nodes and their connections (e.g., A B 3 for A connected to B with a cost of 3):")
    print("Type 'done' when finished.")
    
    while True:
        edge = input("Enter edge (or 'done'): ").strip()
        if edge.lower() == 'done':
            break
        
        try:
            node1, node2, cost = edge.split()
            cost = int(cost)
            if node1 not in graph:
                graph[node1] = {}
            if node2 not in graph:
                graph[node2] = {}
            graph[node1][node2] = cost
            graph[node2][node1] = cost  # Assuming an undirected graph
        except ValueError:
            print("Invalid input! Please enter in the format: Node1 Node2 Cost (e.g., A B 3)")
    
    return graph

def main():
    graph = get_graph_input()
    start = input("Enter the start node: ").strip()
    goal = input("Enter the goal node: ").strip()
    
    path, cost = a_star_algorithm(graph, start, goal, heuristic)
    if path:
        print(f"Shortest path from {start} to {goal}: {path}")
        print(f"Total cost of the path: {cost}")
    else:
        print(f"No path found from {start} to {goal}")

if __name__ == "__main__":
    main()
