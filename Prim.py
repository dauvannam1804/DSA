import queue
INF = 1e9

class Node:
    def __init__(self, id, dist):
        self.dist = dist
        self.id = id

    def __lt__(self, other):
        return self.dist <= other.dist
    
def printMST(n, path, dist):
    ans = 0
    for i in range(n):
        if path[i] == -1:
            continue

        ans += dist[i]
        print("{0} - {1}: {2}".format(path[i], i, dist[i]))
    print("Weight of MST: {0}".format(ans))

def prims(src, dist, visited, graph, path):
    pq = queue.PriorityQueue()
    pq.put(Node(src, 0))
    dist[src] = 0

    while pq.empty() == False:
        top = pq.get()
        u = top.id
        visited[u] = True
        
        for neighbor in graph[u]:
            v = neighbor.id
            w = neighbor.dist
            if visited[v] == False and w < dist[v]:
                dist[v] = w
                pq.put(Node(v, w))
                path[v] = u

if __name__ == "__main__":
    n, m = map(int, input().split())
    graph = [[] for i in range(n)]
    dist = [INF for i in range(n)]
    path = [-1 for i in range(n)]
    visited = [False for i in range(n)]

    for i in range(m):
        u, v, w = map(int, input().split())
        graph[u].append(Node(v, w))
        graph[v].append(Node(u, w))

    prims(0, dist, visited, graph, path)
    printMST(n, path, dist)


'''
# INPUT
6 9
0 1 -2
0 3 9
1 2 3
1 3 8
1 4 5
1 5 -1
2 5 5
3 4 3
4 5 7

# OUTPUT
0 - 1: -2
1 - 2: 3
4 - 3: 3
1 - 4: 5
1 - 5: -1
weight = 8
'''