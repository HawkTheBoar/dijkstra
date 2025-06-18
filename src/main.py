from dijkstra import dijkstra
if __name__ == "__main__":
    vertices = 6
    source = 0
    edges = [
        (0, 1, 3),
        (0, 5, 10),
        (1, 2, 3),
        (2, 3, 1),
        (2, 4, 4),
        (3, 4, 4),
        (5, 4, 2),
        (5, 2, 8)
    ]
    print(dijkstra(edges, vertices, 0))
