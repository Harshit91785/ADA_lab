
# Program 7: Shortest Path Algorithms

# ---------- Dijkstra's Algorithm ----------
def dijkstra(graph, src):
    n = len(graph)

    # Initialize distances to infinity
    dist = [float('inf')] * n
    visited = [False] * n
    dist[src] = 0

    # Find shortest distance for each vertex
    for _ in range(n):
        u = -1

        # Select the unvisited vertex with minimum distance
        for i in range(n):
            if not visited[i] and (
                u == -1 or dist[i] < dist[u]
            ):
                u = i

        # Stop if remaining vertices are unreachable
        if u == -1 or dist[u] == float('inf'):
            break

        visited[u] = True

        # Update distances of neighboring vertices
        for v in range(n):
            if graph[u][v] != 0 and not visited[v]:
                if dist[u] + graph[u][v] < dist[v]:
                    dist[v] = dist[u] + graph[u][v]

    return dist


# ---------- Bellman-Ford Algorithm ----------
def bellman_ford(vertices, edges, src):
    # Initialize distances
    dist = [float('inf')] * vertices
    dist[src] = 0

    # Relax all edges V-1 times
    for _ in range(vertices - 1):
        changed = False

        for u, v, weight in edges:
            if dist[u] != float('inf'):
                if dist[u] + weight < dist[v]:
                    dist[v] = dist[u] + weight
                    changed = True

        # Stop if no distance changes
        if not changed:
            break

    # Check for a negative-weight cycle
    for u, v, weight in edges:
        if dist[u] != float('inf'):
            if dist[u] + weight < dist[v]:
                return "Negative-weight cycle detected"

    return dist


# ---------- Main Program ----------
print("PROGRAM 7")
print("Shortest Path Algorithms")

# Graph for Dijkstra's algorithm
graph = [
    [0, 4, 1, 0, 0],
    [0, 0, 0, 1, 0],
    [0, 2, 0, 5, 0],
    [0, 0, 0, 0, 3],
    [0, 0, 0, 0, 0]
]

print("\nDijkstra's Algorithm")
print("Source Vertex = 0")
print("Distances =", dijkstra(graph, 0))

# Graph edges for Bellman-Ford
edges = [
    (0, 1, 4),
    (0, 2, 1),
    (2, 1, 2),
    (1, 3, 1),
    (2, 3, 5),
    (3, 4, 3)
]

print("\nBellman-Ford Algorithm")
print("Source Vertex = 0")
print("Distances =", bellman_ford(5, edges, 0))
