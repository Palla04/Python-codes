from collections import deque

# BFS from given source s until reaching the end vertex
def bfs(adj, s_index, end_index, index_to_vertex):
    # Create a queue for BFS
    q = deque()
    visited = [False] * len(adj)
    parent = [-1] * len(adj)  # To reconstruct the path
    visited[s_index] = True
    q.append(s_index)

    while q:
        curr = q.popleft()

        # Stop traversal if the end vertex is reached
        if curr == end_index:
            break

        # Explore adjacent vertices
        for neighbor in adj[curr]:
            if not visited[neighbor]:
                visited[neighbor] = True
                parent[neighbor] = curr  # Record parent to reconstruct the path
                q.append(neighbor)

    # Reconstruct the path from start to end vertex
    path = []
    curr = end_index
    while curr != -1:
        path.append(index_to_vertex[curr])
        curr = parent[curr]
    
    return path[::-1]  # Return reversed path

def add_edge(adj, u_index, v_index):
    adj[u_index].append(v_index)
    adj[v_index].append(u_index)

def main():
    input_filename = "input.txt"
    output_filename = "output.txt"
    
    vertex_to_index = {}
    index_to_vertex = []

    with open(input_filename, 'r') as file:
        V = int(file.readline().strip())
        adj = [[] for _ in range(V)]
        E = int(file.readline().strip())

        for _ in range(E):
            u, v = file.readline().strip().split()
            if u not in vertex_to_index:
                vertex_to_index[u] = len(index_to_vertex)
                index_to_vertex.append(u)
            if v not in vertex_to_index:
                vertex_to_index[v] = len(index_to_vertex)
                index_to_vertex.append(v)
            add_edge(adj, vertex_to_index[u], vertex_to_index[v])

        start_vertex = file.readline().strip()
        end_vertex = file.readline().strip()

        if start_vertex not in vertex_to_index or end_vertex not in vertex_to_index:
            print(f"Error: Start or end vertex not in graph.")
            return

        start_index = vertex_to_index[start_vertex]
        end_index = vertex_to_index[end_vertex]

    # Find the path using BFS
    path = bfs(adj, start_index, end_index, index_to_vertex)

    # Write output to output.txt
    with open(output_filename, 'w') as file:
        file.write(" -> ".join(path) + "\n")

if __name__ == "__main__":
    main()
