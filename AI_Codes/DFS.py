def DFS_Visit(u, G, color, p, D, F, time):
    color[u] = 'g'  # Mark the current node as "gray" (visited but not fully explored)
    time[0] += 1
    D[u] = time[0]  # Set discovery time
    
    print(f"\nVisited: {u}")

    for i in range(1, len(G)):
        if G[u][i] and color[i] == 'w':  # Check if there's an edge and the node is unvisited
            p[i] = u  # Set parent
            DFS_Visit(i, G, color, p, D, F, time)
    
    color[u] = 'b'  # Mark node as fully explored
    time[0] += 1
    F[u] = time[0]  # Set finishing time


def DFS(G, n):
    color = ['w'] * (n + 1)  # Colors of nodes ('w' = white, 'g' = gray, 'b' = black)
    p = [0] * (n + 1)  # Parent array
    D = [0] * (n + 1)  # Discovery times
    F = [0] * (n + 1)  # Finishing times
    time = [0]  # Time counter, list to allow pass by reference

    for i in range(1, n + 1):
        if color[i] == 'w':  # Unvisited node
            DFS_Visit(i, G, color, p, D, F, time)

    # Display results
    for i in range(1, n + 1):
        print(f"\nVertex: {i} | Discovery time: {D[i]} | Finishing time: {F[i]} | Color: {color[i]} | Parent: {p[i]}")


def main():
    n = int(input("Enter number of vertices: "))
    e = int(input("Enter number of edges: "))

    # Initialize adjacency matrix
    G = [[0] * (n + 1) for _ in range(n + 1)]

    for i in range(1, e + 1):
        u, v = map(int, input("Enter the graph edge (u v): ").split())
        G[u][v] = 1

    DFS(G, n)


if __name__ == "__main__":
    main()
