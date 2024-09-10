# # https://vjudge.net/problem/UVA-10608


def findSet(parent, x):
    if parent[x] != x:
        parent[x] = findSet(parent, parent[x])
    return parent[x]

def unionSet(parent, ranks, u, v):
    if ranks[u] > ranks[v]:
        parent[v] = u
        ranks[u] += ranks[v]
    
    else:
        parent[u] = v
        ranks[v] += ranks[u]

T = int(input())

for _ in range(T):
    N, M = map(int, input().split())

    parent = [i for i in range(N + 1)]
    ranks = [1] * (N + 1)
    
    for _ in range(M):
        u, v = map(int, input().split())
        u = findSet(parent, u)
        v = findSet(parent, v)
        if u != v:
            unionSet(parent, ranks, u, v)
        
    print(max(ranks))
