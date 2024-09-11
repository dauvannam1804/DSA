# https://vjudge.net/problem/SPOJ-LOSTNSURVIVED

def findSet(parent, u):
    if parent[u] != u:
        parent[u] = findSet(parent, parent[u])
    return parent[u]


N, Q = map(int, input().split())

minGroup, maxGroup = 1, 1

parent, groupSizes, numPeople = [], [], []

for i in range(N + 1):
    parent.append(i)
    groupSizes.append(1)
    numPeople.append(0)

res, numPeople[1] = "", N

for _ in range(Q):
    A, B = map(int, input().split())
    pA, pB = findSet(parent, A), findSet(parent, B)

    if pA != pB:
        numPeople[groupSizes[pA]] -= 1
        numPeople[groupSizes[pB]] -= 1
        groupSizes[pA] += groupSizes[pB]
        numPeople[groupSizes[pA]] += 1
        parent[pB], maxGroup = pA, max(maxGroup, groupSizes[pA])

        while numPeople[minGroup] == 0: 
            minGroup += 1

    res += f"{maxGroup - minGroup}\n"

print(res)