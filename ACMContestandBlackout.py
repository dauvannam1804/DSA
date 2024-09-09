import heapq

INF = 1e9

def prim(N, graph, trace, needTrace):
    dist = [INF] * N
    visited = [False] * N

    mst = 0
    pq = []
    heapq.heappush(pq, (0, 0))
    dist[0] = 0
    
    while pq:
        current_dist, u = heapq.heappop(pq)

        if visited[u]: continue
        visited[u] = True

        for i in range(len(graph[u])):
            v, w = graph[u][i]
            if not visited[v] and w < dist[v]:
                dist[v] = w
                heapq.heappush(pq, (w, v))
                if needTrace:
                    trace[v][0] = u
                    trace[v][1] = i
    
    for i in range(N): mst += dist[i]
    return mst

T = int(input())

for _ in range(T):
    N, M = map(int, input().split())

    graph = [[] for _ in range(N)]
    trace = [[0, 0] for _ in range(N)]

    for _ in range(M):
        A, B, C = map(int, input().split())
        A -= 1
        B -= 1
        graph[A].append((B, C))
        graph[B].append((A, C))


    mst1 = prim(N, graph, trace, True)
    mst2 = INF

    for v in range(1, N):
        u = trace[v][0]
        i = trace[v][1]

        tmp = graph[u][i]
        graph[u][i] = (v, INF)
        mst2 = min(mst2, prim(N, graph, trace, False))
        graph[u][i] = tmp

    print(mst1, mst2)


