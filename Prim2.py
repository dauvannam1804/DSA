import queue

INF = 1e9

def prims(src, dist, visited, graph):
    pq = queue.PriorityQueue()
    pq.put((0, src))
    dist[src] = 0
    total_weight = 0

    while not pq.empty():
        current_dist, u = pq.get()
        
        if visited[u]:
            continue
        
        visited[u] = True
        total_weight += current_dist

        for v, w in graph[u]:
            if not visited[v] and w < dist[v]:
                dist[v] = w
                # path[v] = u
                pq.put((w, v))

    return total_weight

# def printMST(n, path, dist):
#     ans = 0
#     for i in range(n):
#         if path[i] != -1:
#             ans += dist[i]
#             # print("{0} - {1}: {2}".format(path[i], i, dist[i]))
#     # print("Weight of MST: {0}".format(ans))

n, m = map(int, input().split())
graph = [[] for _ in range(n)]
dist = [INF] * n
# path = [-1] * n
visited = [False] * n

for _ in range(m):
    u, v, w = map(int, input().split())
    u = u - 1
    v = v - 1
    graph[u].append((v, w))
    graph[v].append((u, w))

print(prims(0, dist, visited, graph))
# print(printMST(n, path, dist))
