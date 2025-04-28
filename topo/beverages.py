# https://vjudge.net/problem/UVA-11060

import sys
import heapq

def main():
    case_num = 1
    lines = sys.stdin.read().splitlines()
    idx = 0
    while idx < len(lines):
        if lines[idx] == '':
            idx += 1
            continue
        N = int(lines[idx])
        idx += 1
        drinks = []
        drink_index = dict()
        for i in range(N):
            name = lines[idx].strip()
            drinks.append(name)
            drink_index[name] = i
            idx += 1
        M = int(lines[idx])
        idx += 1
        adj = [[] for _ in range(N)]
        in_degree = [0] * N
        for _ in range(M):
            u, v = lines[idx].strip().split()
            u_idx = drink_index[u]
            v_idx = drink_index[v]
            adj[u_idx].append(v_idx)
            in_degree[v_idx] += 1
            idx += 1

        heap = []
        for i in range(N):
            if in_degree[i] == 0:
                heapq.heappush(heap, i)

        order = []
        while heap:
            u = heapq.heappop(heap)
            order.append(drinks[u])
            for v in adj[u]:
                in_degree[v] -= 1
                if in_degree[v] == 0:
                    heapq.heappush(heap, v)

        print("Case #{}: Dilbert should drink beverages in this order: {}.".format(case_num, ' '.join(order)))
        print()
        case_num += 1

if __name__ == "__main__":
    main()


# Run code on python3 3.5.1
# Test cases
"""
3
vodka
wine
beer
2
wine vodka
beer wine

5
wine
beer
rum
apple-juice
cachaca
6
beer cachaca
apple-juice beer
apple-juice rum
beer rum
beer wine
wine cachaca

10
cachaca
rum
apple-juice
tequila
whiskey
wine
vodka
beer
martini
gin
11
beer whiskey
apple-juice gin
rum cachaca
vodka tequila
apple-juice martini
rum gin
wine whiskey
apple-juice beer
beer rum
wine vodka
beer tequila

"""
