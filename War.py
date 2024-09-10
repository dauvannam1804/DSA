# https://vjudge.net/problem/UVA-10158

MAX = 10000

def findSet(parent, u):
    if parent[u] != u:
        parent[u] = findSet(parent, parent[u])
    return parent[u]

def unionSet(parent, ranks, u, v):
    pu = findSet(parent, u)
    pv = findSet(parent, v)

    if pu == pv: return
    if ranks[pu] > ranks[pv]:
        parent[pv] = pu
    elif ranks[pu] < ranks[pv]:
        parent[pu] = pv
    else:
        parent[pu] = pv
        ranks[pv] += 1
 
def areFriends(parent, x, y):
    return findSet(parent, x) == findSet(parent, y)

def areEnemies(parent, x, y):
    return areFriends(parent, x, y + MAX)


n = int(input())
parent = [i for i in range(MAX * 2)]
ranks = [0] * (MAX * 2)

while True:
    c, x, y = map(int, input().split())
    if c+x+y == 0: break
    if c==1:
        if areEnemies(parent, x, y):
            print(-1)
        else:
            unionSet(parent, ranks, x, y)
            unionSet(parent, ranks, x + MAX, y + MAX)
    
    elif c==2:
        if areFriends(parent, x, y):
            print(-1)
        else:
            unionSet(parent, ranks, x, y + MAX)
            unionSet(parent, ranks, x + MAX, y)

    elif c==3:
        if areFriends(parent, x, y):
            print(1)
        else:
            print(0)

    elif c==4:
        if areEnemies(parent, x, y):
            print(1)
        else:
            print(0)


""" 
10
1 0 1
1 1 2
2 0 5
3 0 2
3 8 9
4 1 5
4 1 2
4 8 9
1 8 9
1 5 2
3 5 2
0 0 0
"""