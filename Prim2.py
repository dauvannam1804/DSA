import queue

INF = 1e9

def prims(src, dist, visited, graph):
    pq = queue.PriorityQueue()
    pq.put((0, src))
    dist[src] = 0

    while not pq.empty():
        current_dist, u = pq.get()
        
        if visited[u]:
            continue
        
        visited[u] = True

        for v, w in graph[u]:
            if not visited[v] and w < dist[v]:
                dist[v] = w
                pq.put((w, v))

n, m = map(int, input().split())
graph = [[] for _ in range(n)]
dist = [INF] * n
visited = [False] * n

for _ in range(m):
    u, v, w = map(int, input().split())
    u = u - 1
    v = v - 1
    graph[u].append((v, w))
    graph[v].append((u, w))

prims(0, dist, visited, graph)
sumMST = 0
for i in range(n):
    sumMST += dist[i]
print(sumMST)
