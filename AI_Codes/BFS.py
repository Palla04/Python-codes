# DFS function
def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()  # To store visited nodes

    # Mark the current node as visited and print it
    visited.add(start)
    print(start, end=' ')

    # Recur for all the vertices adjacent to this vertex
    for neighbor in graph[start]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)

# Example graph represented as an adjacency list (dictionary)
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

# Example usage: Perform DFS starting from node 'A'
print("DFS traversal starting from node 'A':")
dfs(graph, 'A')