# https://codeforces.com/problemset/problem/217/A

def findSet(parent, u):
    if parent[u] != u:
        parent[u] = findSet(parent, parent[u])
    return parent[u]

def unionSet(parent, ranks, u, v):
    pu = findSet(parent, u)
    pv = findSet(parent, v)

    if pu == pv: return

    if ranks[pu] < ranks[pv]:
        parent[pu] = pv
    elif ranks[pu] > ranks[pv]:
        parent[pv] = pu
    else:
        parent[pv] = pu
        ranks[pu] += 1



n = int(input())

coors = []

for _ in range(n):
    x, y = map(int, input().split())
    coors.append((x, y))

parent = [i for i in range(n + 2001)]
ranks = [0] * (n + 2001)

for i, (x, y) in enumerate(coors):
        unionSet(parent, ranks, i, x + n)
        unionSet(parent, ranks, i, y + n + 1000)

components = set(findSet(parent, i) for i in range(n))
print(len(components) - 1)