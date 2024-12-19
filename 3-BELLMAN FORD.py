def add_edge(graph, u, v, w):
    graph.append([u, v, w])

def print_solution(dist, vertices):
    print("Vertex Distance from Source")
    for i in range(vertices):
        print(f"{i}\t\t{dist[i]}")

def bellman_ford(vertices, edges, graph, src):
    dist = [float("Inf")] * vertices
    dist[src] = 0

    for _ in range(vertices - 1):
        for u, v, w in graph:
            if dist[u] != float("Inf") and dist[u] + w < dist[v]:
                dist[v] = dist[u] + w

    for u, v, w in graph:
        if dist[u] != float("Inf") and dist[u] + w < dist[v]:
            print("Graph contains a negative weight cycle")
            return

    print_solution(dist, vertices)


def main():
    vertices = int(input("Enter number of vertices: "))
    edges = int(input("Enter number of edges: "))
    
    graph = []  
    
    print("Enter the edges with start vertex, end vertex, and weight:")
    for i in range(1, edges + 1):
        print(f"Edge {i}:")
        u = int(input("Enter start vertex: "))
        v = int(input("Enter end vertex: "))
        w = int(input("Enter weight of the edge: "))
        
        add_edge(graph, u, v, w)
    
    src = int(input("Enter the source vertex: "))
    
    if src < 0 or src >= vertices:
        print("Invalid source vertex. It must be between 0 and", vertices - 1)
        return
    
    bellman_ford(vertices, edges, graph, src)


if __name__ == "__main__":
    main()
