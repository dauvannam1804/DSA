# https://vjudge.net/problem/SPOJ-CSTREET

import heapq

INF = 1e9

def prims(src, graph, dist, visited):
    pq = []
    heapq.heappush(pq, (0, src))
    dist[src] = 0
    while pq:
        current_dist, u = heapq.heappop(pq)
        if visited[u]: continue

        visited[u] = True

        for v, w in graph[u]:
            if not visited[v] and w < dist[v]:
                dist[v] = w
                heapq.heappush(pq, (w, v))


t = int(input())

for _ in range(t):
    p = int(input())
    n = int(input())
    m = int(input())

    graph = [[] for _ in range(n)]
    visited = [False] * n
    dist = [INF] * n

    for _ in range(m):
        a, b, c = map(int, input().split())
        a-=1
        b-=1
        graph[a].append((b, c))
        graph[b].append((a, c))

    prims(0, graph, dist, visited)
    
    sumMST = 0
    for i in dist:
        sumMST += i
    
    print(sumMST * p)