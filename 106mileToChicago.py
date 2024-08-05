from math import log, exp

INF = float("inf")

def BellmanFord(graph, dist, n, m):
    dist[0] = 0
    for i in range(1, n):
        # print(f" === LOOP {i} ===")
        for u, v, w in graph:
            # print(u, v, w)
            if dist[u] != INF and dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
            # print(dist)

while True:
    line = list(map(int, input().split()))
    if line[0] == 0:
        break
    n, m = line
    graph = []
    dist = [INF for _ in range(n)]


    for _ in range(m):
        a, b, p = map(int, input().split())
        p = log(100/p)
        graph.append((a - 1, b - 1, p))
        graph.append((b - 1 , a - 1 , p))

    # print(graph)
    # print(graph[0][2] * 1)
    # print(dist)
    BellmanFord(graph, dist, n, m)
    print(f"{exp(log(100)-dist[n - 1]):.6f} percent")
"""
5 7
5 2 100
3 5 80
2 3 70
2 1 50
3 4 90
4 1 85
3 1 70
0
"""
