def dfs_visit(graph, u, color, discovery, finish, parent, time):
    print(f"Visited: {u}")
    color[u] = 'g'  # Gray: visiting
    discovery[u] = time[0]
    time[0] += 1
    
    for v in range(len(graph)):
        if graph[u][v] == 1 and color[v] == 'w':  # White: unvisited
            parent[v] = u
            dfs_visit(graph, v, color, discovery, finish, parent, time)
    
    color[u] = 'b'  # Black: fully explored
    finish[u] = time[0]
    time[0] += 1

def dfs(graph, n):
    color = ['w'] * n  # All vertices initially white
    parent = [None] * n
    discovery = [-1] * n
    finish = [-1] * n
    time = [0]  # Shared mutable time counter
    
    for u in range(n):
        if color[u] == 'w':  # Start DFS from unvisited node
            dfs_visit(graph, u, color, discovery, finish, parent, time)
    
    # Print results
    for u in range(n):
        print(f"Vertex: {u}, Discovery time: {discovery[u]}, Finish time: {finish[u]}, Color: {color[u]}, Parent: {parent[u]}")
    
# Main function
if __name__ == "__main__":
    n = int(input("Enter number of vertices: "))
    e = int(input("Enter the number of edges: "))
    
    # Initialize adjacency matrix
    graph = [[0 for _ in range(n)] for _ in range(n)]
    
    for _ in range(e):
        u, v = map(int, input("Enter the edge (u v): ").split())
        graph[u][v] = 1  # Assuming a directed graph
    
    dfs(graph, n)
