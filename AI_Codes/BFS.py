from collections import deque

# BFS from given source s
def bfs(adj, s):
    # Create a queue for BFS
    q = deque()

    # Initially mark all the vertices as not visited
    visited = [False] * len(adj)

    # Mark the source node as visited and enqueue it
    visited[s] = True
    q.append(s)

    # Iterate over the queue
    while q:
        # Dequeue a vertex from queue and print it
        curr = q.popleft()
        print(curr, end=" ")

        # Get all adjacent vertices of the dequeued vertex.
        # If an adjacent has not been visited, mark it visited and enqueue it
        for x in adj[curr]:
            if not visited[x]:
                visited[x] = True
                q.append(x)

# Function to add an edge to the graph
def add_edge(adj, u, v):
    adj[u].append(v)
    adj[v].append(u)

# Main function to handle user input
if __name__ == "__main__":
    # Number of vertices in the graph
    V = int(input("Enter the number of vertices: "))

    # Adjacency list representation of the graph
    adj = [[] for _ in range(V)]

    # Number of edges in the graph
    E = int(input("Enter the number of edges: "))

    # Add edges to the graph
    print("Enter the edges (u v):")
    for _ in range(E):
        u, v = map(int, input().split())
        add_edge(adj, u, v)

    # Starting vertex for BFS traversal
    start_vertex = int(input("Enter the starting vertex for BFS: "))

    # Perform BFS traversal starting from the given vertex
    print(f"BFS starting from {start_vertex}: ")
    bfs(adj, start_vertex)
