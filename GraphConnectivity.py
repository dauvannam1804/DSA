# https://vjudge.net/problem/UVA-459

def char2int(char):
    return ord(char) - ord("A")

def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]

def union(parent, ranks, u, v):
    pu = find(parent, u)
    pv = find(parent, v)
    if pu == pv: return
    if ranks[pu] > ranks[pv]:
        parent[pv] = pu
    elif ranks[pu] < ranks[pv]:
        parent[pu] = pv
    else:
        parent[pu] = pv
        ranks[pv] += 1

T = int(input())
input()

for case in range(T):
    n = char2int(input().strip()) + 1
    parent = list(range(n))
    ranks = [0] * n

    while True:
        try:
            line = input().strip()
        except EOFError: break
        if line == '': break
        else:
            u, v = char2int(line[0]), char2int(line[1])
            union(parent, ranks, u, v)

    res = set(find(parent, i) for i in range(n))
    print(len(res))
    
    if case < T - 1:
        print()


""" 
2

E
AB
CE
DB
EC

E
AB
CE
DB
EC
"""