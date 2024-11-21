import heapq

def dij(graph,s,d):
    distance={}
    for vertex in graph:
        distance[vertex] = float('inf')
        
    distance[s]=0
    
    priority_queue = [(0,s)]
    path={}
    
    for vertex in graph:
        path[vertex]=[]
    
    path[s]=[s]
    
    while priority_queue:
        current_distance,curr_ver=heapq.heappop(priority_queue)
        
        if curr_ver==d:
            print(f"Sortest path b/w {s} & {d} is {current_distance}")
            print(f"Path: {path[curr_ver]}")
            return
        
        for neig,weight in graph[curr_ver].items():
            new_distance = current_distance+weight
            
            if new_distance<distance[neig]:
                distance[neig]=new_distance
                heapq.heappush(priority_queue, (new_distance, neig))
                path[neig]=path[curr_ver]+[neig]
            
    print(f"No path exists from {s} to {d}.")
            

if __name__ == "__main__":
    n = int(input("Enter the number of vertex: "))
    e = int(input("Enter the number of edge: "))
    
    graph = {}
    
    for _ in range(e):
        u,v,w = map(int, input("Enter the edge(u v w): ").split())
        if u not in graph:
            graph[u] = {}
        if v not in graph:
            graph[v] = {}
        
        graph[u][v] = w
        graph[v][u] = w

        
    source = int(input("Enter the source vertex:"))
    des=int(input("Enter the destination: "))
    dij(graph,source,des)