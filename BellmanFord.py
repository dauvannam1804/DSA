INF = float('inf')

def PrintPath(path, s, t):
    if t == s: 
        print(t, end=" ")
        return
    else:
        if path[t] == -1:
            print("NO PATH", end=" ")
        else:
            PrintPath(path, s, path[t])
            print(t, end=" ")

def BellmanFord(graph, dist, path, n, m):
    # Iterate over n - 1 vertices
    dist[s] = 0
    for i in range(1, n):
        for j in range(m):
            u, v, w = graph[j]
            if dist[u] != INF and dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                path[v] = u
    
    # Check for negative weight cycles
    for i in range(m):
        u, v, w = graph[i]
        if dist[u] != INF and dist[u] + w < dist[v]:
            return False
    return True


if __name__ == '__main__':
    n, m = map(int, input().split())
    dist = [INF for _ in range(n)]
    path = [-1 for _ in range(n)]
    graph = []

    for i in range(m):
        u, v, w = map(int, input().split())
        graph.append((u, v, w))
    
    s, t = 0, 4

    res = BellmanFord(graph, dist, path, n, m)
    
    if not res:
        print("Graph contains negative weight cycle")
    else:
        print("PATH:")
        PrintPath(path, s, t)
        print("\nCost:", dist[t])

'''
6 10
0 1 1
1 2 5
1 3 -2
1 5 7
2 5 -1
3 0 2
3 2 -1
3 4 4
4 3 3
5 4 1
'''