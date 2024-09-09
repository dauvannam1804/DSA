# https://vjudge.net/problem/LightOJ-1041

import heapq
from collections import defaultdict

def prim(graph):
    # Chọn một đỉnh bất kỳ để bắt đầu
    start_vertex = next(iter(graph))
    # print("start_vertex: ", start_vertex)
    visited = set([start_vertex])
    # print("visited: ", visited)
    edges = [
        (cost, start_vertex, to)
        for to, cost in graph[start_vertex]
    ]
    heapq.heapify(edges)
    # print("edge: ", edges)
    total_cost = 0
    while edges:
        cost, frm, to = heapq.heappop(edges)
        if to not in visited:
            visited.add(to)
            # mst.add((frm, to, cost))
            if cost > 0:  # Chỉ tính chi phí nếu đường cần sửa chữa
                total_cost += cost

            for next_to, next_cost in graph[to]:
                if next_to not in visited:
                    heapq.heappush(edges, (next_cost, to, next_to))

    # Kiểm tra xem tất cả các thành phố đã được kết nối chưa
    if len(visited) == len(graph):
        return total_cost
    else:
        return "Impossible"

def solve_case():
    m = int(input())
    graph = defaultdict(list)
    
    for _ in range(m):
        city1, city2, cost = input().split()
        cost = int(cost)
        graph[city1].append((city2, cost))
        graph[city2].append((city1, cost))
    
    # print("GRAPH:", graph)
    return prim(graph)

T = int(input())
for case in range(1, T + 1):
    input()  # Blank line
    result = solve_case()
    print(f"Case {case}: {result}")


"""  
1

12
Dhaka Sylhet 0
Ctg Dhaka 0
Sylhet Chandpur 9
Ctg Barisal 9
Ctg Rajshahi 9
Dhaka Sylhet 9
Ctg Rajshahi 3
Sylhet Chandpur 5
Khulna Rangpur 7
Chandpur Rangpur 7
Dhaka Rajshahi 6
Dhaka Rajshahi 7


2

12
Dhaka Sylhet 0
Ctg Dhaka 0
Sylhet Chandpur 9
Ctg Barisal 9
Ctg Rajshahi 9
Dhaka Sylhet 9
Ctg Rajshahi 3
Sylhet Chandpur 5
Khulna Rangpur 7
Chandpur Rangpur 7
Dhaka Rajshahi 6
Dhaka Rajshahi 7

2
Rajshahi Khulna 4
Kushtia Bhola 1
"""