# https://www.spoj.com/problems/MAKETREE/

from collections import deque
import sys
sys.setrecursionlimit(200000)

def bfs(start, graph, n):
    dist = [-1] * (n + 1)
    q = deque()
    q.append(start)
    dist[start] = 0
    while q:
        u = q.popleft()
        for v in graph[u]:
            if dist[v] == -1:
                dist[v] = dist[u] + 1
                q.append(v)
    return dist

def solve():
    n, m, d = map(int, input().split())
    affected = list(map(int, input().split()))

    # Build graph
    graph = [[] for _ in range(n + 1)]
    for _ in range(n - 1):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)

    # Step 1: BFS from any affected node to find farthest affected
    dist1 = bfs(affected[0], graph, n)
    print(dist1)
    farthest = affected[0]
    max_dist = -1
    for p in affected:
        if dist1[p] > max_dist:
            max_dist = dist1[p]
            farthest = p

    # Step 2: BFS from farthest affected node to find other end of "diameter"
    dist_u = bfs(farthest, graph, n)
    print(dist_u)
    farthest2 = affected[0]
    max_dist = -1
    for p in affected:
        if dist_u[p] > max_dist:
            max_dist = dist_u[p]
            farthest2 = p

    # Step 3: BFS from second farthest affected node
    dist_v = bfs(farthest2, graph, n)
    print(dist_v)

    # Step 4: check for each node
    result = 0
    for i in range(1, n + 1):
        if max(dist_u[i], dist_v[i]) <= d:
            result += 1

    print(result)

# Run the solution
solve()


