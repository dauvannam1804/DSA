from heapq import heappush, heappop
INF = 10 ** 9 + 7

def Dijkstra(s, f, dist):
    pq = [(0, s)]
    dist[s] = 0
    
    while pq:
        w, u = heappop(pq)
        if u == f:
            break
        
        if w > dist[u]:
            continue
        
        for weight, v in graph[u]:
            if w + weight < dist[v]:
                dist[v] = w + weight
                heappush(pq, (dist[v], v))

N = int(input())

for t in range(1, N + 1):
    n, m, S, T = map(int, input().split())
    graph = [[] for _ in range(n)]
    
    for _ in range(m):
        u, v, w = map(int, input().split())
        graph[u].append((w, v))
        graph[v].append((w, u))
    
    dist = [INF] * n
    Dijkstra(S, T, dist)
    
    print('Case #{}: '.format(t), end='')
    print(dist[T] if dist[T] != INF else "unreachable")

'''
3
2 1 0 1
0 1 100
3 3 2 0
0 1 100
0 2 200
1 2 50
2 0 0 1

'''