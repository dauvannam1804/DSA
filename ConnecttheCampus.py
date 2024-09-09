# https://vjudge.net/problem/UVA-10397

import math
import heapq

class Scanner:
    def __generator__():
        while True:
            try:
                buff = input().strip().split()
                for x in buff:
                    yield x
            except EOFError:
                exit()

    sc = __generator__()
    def next():
        return Scanner.sc.__next__()

# Hàm tính khoảng cách Euclidean giữa hai tòa nhà
def distance(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

# Hàm giải bài toán bằng thuật toán Prim
def prim_mst(n, buildings, existing_cables):
    dist = [float('inf')] * n
    visited = [False] * n
    pq = []
    
    # Bắt đầu từ tòa nhà đầu tiên
    heapq.heappush(pq, (0, 0))
    dist[0] = 0
    total_cost = 0

    # Đánh dấu các tòa nhà đã kết nối bằng cáp có sẵn
    adj = [[distance(buildings[i], buildings[j]) for j in range(n)] for i in range(n)]
    for u, v in existing_cables:
        adj[u][v] = adj[v][u] = 0

    while pq:
        current_dist, u = heapq.heappop(pq)

        if visited[u]:
            continue
        
        visited[u] = True
        total_cost += current_dist
        
        # Duyệt các cạnh nối với tòa nhà u
        for v in range(n):
            if not visited[v] and adj[u][v] < dist[v]:
                dist[v] = adj[u][v]
                heapq.heappush(pq, (adj[u][v], v))
    
    return total_cost

# Đọc input
def solve():
    while True:
        try:
            n = int(Scanner.next())
            buildings = []
            for _ in range(n):
                x, y = int(Scanner.next()), int(Scanner.next())
                buildings.append((x, y))
            
            m = int(Scanner.next())
            existing_cables = []
            for _ in range(m):
                u, v = int(Scanner.next()), int(Scanner.next())
                existing_cables.append((u - 1, v - 1))  # chuyển sang chỉ số 0-based
            
            # Tính và in ra kết quả, làm tròn đến 2 chữ số thập phân
            result = prim_mst(n, buildings, existing_cables)
            print(f"{result:.2f}")
        
        except EOFError:
            break

solve()

""" 
4
103 104
104 100
104 103
100 100
1
4 2
4
103 104
104 100
104 103
100 100
1
4 2


"""