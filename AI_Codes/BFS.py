from collections import deque

def bfs(graph, n):
    color = ['w'] * n  # All vertices initially white
    discovery = [-1] * n  # Discovery time
    parent = [None] * n  # Parent of each vertex
    time = 0  # Time counter

    for start in range(n):
        if color[start] == 'w':  # Start BFS from unvisited node
            queue = deque([start])
            color[start] = 'g'  # Mark as discovered
            discovery[start] = time
            time += 1

            while queue:
                u = queue.popleft()
                print(f"Visited: {u}")
                
                for v in range(n):
                    if graph[u][v] == 1 and color[v] == 'w':  # Unvisited neighbor
                        color[v] = 'g'
                        parent[v] = u
                        discovery[v] = time
                        time += 1
                        queue.append(v)

                color[u] = 'b'  # Fully processed

    # Print results
    for u in range(n):
        print(f"Vertex: {u}, Discovery time: {discovery[u]}, Color: {color[u]}, Parent: {parent[u]}")

# Main function
if __name__ == "__main__":
    n = int(input("Enter number of vertices: "))
    e = int(input("Enter the number of edges: "))
    
    # Initialize adjacency matrix
    graph = [[0 for _ in range(n)] for _ in range(n)]
    
    for _ in range(e):
        u, v = map(int, input("Enter the edge (u v): ").split())
        graph[u][v] = 1  # Assuming a directed graph
    
    bfs(graph, n)
