import heapq


def dijkstra(edges, n, source):
    # Build graph as adjacency list
    graph = [[] for _ in range(n)]
    for start, dest, distance in edges:
        graph[start].append((dest, distance))

    # Initialize distances with infinity
    dist = [float('inf')] * n
    dist[source] = 0

    # Priority queue: (distance, vertex)
    heap = [(0, source)]

    while heap:
        d, u = heapq.heappop(heap)
        # Skip outdated entries
        if d != dist[u]:
            continue
        # Update neighbors
        for v, weight in graph[u]:
            new_dist = dist[u] + weight
            if new_dist < dist[v]:
                dist[v] = new_dist
                heapq.heappush(heap, (new_dist, v))

    return dist
