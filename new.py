def bellmanford(V, edges, src):
    dist = [float('inf')] * V
    dist[src] = 0

    for _ in range(V - 1):
        for u, v, w in edges:
            if dist[u] + w < dist[v]:
                dist[v] = dist[u] + w

    for u, v, w in edges:
        if dist[u] + w < dist[v]:
            print("The graph has a negative weight cycle")
            return

    print("Vertex\tDistance")
    for i, d in enumerate(dist):
        print(f"{i}\t{d}")


V = int(input("Vertices: "))
E = int(input("Edges: "))
edges = [tuple(map(int, input("Edge (src, dest, weight): ").split())) for _ in range(E)]  # Changed `edge` to `edges`
src = int(input("Source: "))
bellmanford(V, edges, src)  # Pass the corrected `edges`
