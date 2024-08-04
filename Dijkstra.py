import heapq

INF = int(1e9)

def Dijkstra(s):
    pq = []
    heapq.heapify(pq)
    heapq.heappush(pq, (0, s))
    dist[s] = 0
    while len(pq):
        top = pq[0]
        u = top[1]
        w = top[0]
        heapq.heappop(pq)
        for neighbor in graph[u]:
            if w + neighbor[0] < dist[neighbor[1]]:
                dist[neighbor[1]] = w + neighbor[0]
                heapq.heappush(pq, (dist[neighbor[1]], neighbor[1]))
                path[neighbor[1]] = u

def printPath(s, t):
    if s == t:
        print(t, end=" ")
    else:
        if path[t] == -1:
            print("No path")
        else:
            printPath(s, path[t])
            print(t, end=" ")

if __name__ == "__main__":
    n = int(input())

    s, t = 0, 4

    graph = [[] for _ in range(n)]
    dist = [INF for _ in range(n)]
    path = [-1 for _ in range(n)]

    for i in range(n):
        d = list(map(int, input().split()))
        for j in range(n):
            if d[j] > 0:
                graph[i].append((d[j], j))

    # print(graph)
    Dijkstra(s)
    # print(dist)
    ans = dist[t]
    print("Path: ", end="")
    printPath(s,t)
    print("\nCost:",ans)

'''
6
0 1 0 0 0 0
0 0 5 2 0 7
0 0 0 0 0 1
2 0 1 0 4 0
0 0 0 3 0 0
0 0 0 0 1 0
'''
