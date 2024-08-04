INF = float('inf')

def PrintPath(path, s, f):
    if f == s: 
        print(f, end=" ")
        return
    if path[s][f] == -1:
        print("NO PATH", end=' ')
        return
    PrintPath(path, s, path[s][f])
    print(f, end=" ")

def PrintSolution(graph, dist, V):
    for i in range(V):
        for j in range(V):
            if i != j: 
                print("{} -> {}".format(i, j), end='\n')
                PrintPath(path, i, j)
                print()

            if path[i][j] != -1:
                print("Total length: {}".format(dist[i][j]))

def FloyWarshall(graph, dist, path, V):
    # Make dist matrix
    for i in range(V):
        for j in range(V):
            dist[i][j] = graph[i][j]
            if graph[i][j] != INF and i != j:
                path[i][j] = i
            else:
                path[i][j] = -1

    # Find shortest path between pairs of nodes
    for k in range(V):
        for i in range(V):
            if dist[i][k] == INF:
                continue
            for j in range(V):
                if dist[k][j] != INF and dist[i][j] > dist[i][k] + dist[k][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
                    path[i][j] = path[k][j]

    for i in range(V):
        if dist[i][i] < 0: return False
    return True


if __name__ == '__main__':
    V = int(input())
    graph = [[None for  i in range(V)] for j in range(V)]
    dist = [[None for  i in range(V)] for j in range(V)]
    path = [[None for  i in range(V)] for j in range(V)]

    for i in range(V):
        line = list(map(int, input().split()))
        for j in range(V):
            graph[i][j] = INF if line[j] == 0 and i != j else line[j]

    if FloyWarshall(graph, dist, path, V):
        PrintSolution(path, dist, V)
    else:
        print("Graph contains negative weight cycle")


'''
6
0 1 0 0 0 0
0 0 5 -2 0 7
0 0 0 0 0 -1
2 0 -1 0 4 0
0 0 0 3 0 0
0 0 0 0 1 0
'''