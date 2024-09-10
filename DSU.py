MAX = 20
parent = []

def makeSet():
    global parent
    parent = [i for i in range(MAX + 5)]

def findSet(u):
    while u != parent[u]:
        u = parent[u]
    return u

def unionSet(u, v):
    up = findSet(u)
    vp = findSet(v)
    parent[up] = vp

if __name__ == "__main__":
    Q = int(input())
    makeSet()
    res = ""
    for i in range(Q):
        u, v, q = map(int, input().split())
        if q == 1:
            unionSet(u, v)
        if q == 2:
            parentU = findSet(u)
            parentV = findSet(v)
            if parentU == parentV: 
                # print("YES")
                res += "YES\n"
            else: 
                # print("NO")
                res += "NO\n"

    print(res)
    print(parent)

"""  
# INPUT
9
1 2 1
2 3 1
4 5 1
5 6 1
2 6 2
6 7 1
7 3 1
6 2 2
7 1 2

# OUTPUT
NO
YES
YES

"""