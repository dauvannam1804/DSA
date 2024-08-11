import sys
import math
 
def solve():
    sum = 0
    v = []
    n = int(input())
    N = n + 1
    delete = [0] * N
    graph = [[0] * N for _ in range(N)]
    ans = [0] * N
    
    # Nhập ma trận graph
    for i in range(1, n + 1):
        graph[i][1:n+1] = list(map(int, input().split()))
    
    # Nhập mảng delete
    delete[1:n+1] = list(map(int, input().split()))
    
    for i in range(n, 0, -1):
        print(f"### i = {i} - delete = {delete[i]} ###")
        for k in range(1, n + 1):
            for p in range(1, n + 1):
                if k == p:
                    continue
                graph[k][p] = min(graph[k][p], graph[k][delete[i]] + graph[delete[i]][p])
        
        sum = 0
        for j in range(i, n + 1):
            for k in range(i, n + 1):
                print(f"(j,k)=({j},{k}) - delete[{j}] = {delete[j]}, delete[{k}] = {delete[k]}")
                print(f"graph[{delete[j]}][{delete[k]}] = {graph[delete[j]][delete[k]]}")
                sum += graph[delete[j]][delete[k]]
        
        ans[i] = sum
        for g in graph: print(g)
        print("SUM: ", sum)
    print(" ".join(map(str, ans[1:n+1])))
 
def main():
    t = 1
    while t:
        solve()
        t -= 1
 
if __name__ == "__main__":
    main()