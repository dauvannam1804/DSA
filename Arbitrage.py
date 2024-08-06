from math import log, exp

INF = float("inf")

def FloydWarshall(dist, n):
    for k in range(n):
        for i in range(n):
            for j in range(n):
                new_w = dist[i][k] + dist[k][j]
                if new_w < dist[i][j]:
                    dist[i][j] = new_w

case = 1
while True:
    n = int(input())
    if n == 0: break

    currencies = {}
    for i in range(n):
        c = input()
        currencies[c] = i

    dist = [[INF] * n for _ in range(n)]

    for i in range(n):
        dist[i][i] = 0

    # input()
    m = int(input())
    for _ in range(m):
        line = input().split()
        c1, r, c2 = line[0], -log(float(line[1])), line[2]
        dist[currencies[c1]][currencies[c2]] = r

    # print(dist)
    FloydWarshall(dist, n)
    # print(dist)
    valid = True
    for i in range(n):
        if dist[i][i] >= 0: 
            valid = False
            break

    if valid:
        print(f"Case {case}: Yes")
    else:
        print(f"Case {case}: No")
    case+=1
    input()

"""
3
USDollar
BritishPound
FrenchFranc
3
USDollar 0.5 BritishPound
BritishPound 10.0 FrenchFranc
FrenchFranc 0.21 USDollar

3
USDollar
BritishPound
FrenchFranc
6
USDollar 0.5 BritishPound
USDollar 4.9 FrenchFranc
BritishPound 10.0 FrenchFranc
BritishPound 1.99 USDollar
FrenchFranc 0.09 BritishPound
FrenchFranc 0.19 USDollar

0
"""
