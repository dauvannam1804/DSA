# https://codeforces.com/problemset/problem/770/C

from collections import defaultdict, deque
import sys
sys.setrecursionlimit(200000)

def main():
    n, k = map(int, input().split())
    main_courses = list(map(int, input().split()))

    dependencies = [[] for _ in range(n + 1)]  # 1-based index

    for i in range(1, n + 1):
        parts = list(map(int, input().split()))
        t, prereqs = parts[0], parts[1:]
        dependencies[i] = prereqs

    # Step 1: Find all courses required to learn all main_courses
    needed = set()
    visited = [False] * (n + 1)

    def dfs(course):
        if visited[course]:
            return
        visited[course] = True
        needed.add(course)
        for pre in dependencies[course]:
            dfs(pre)

    for mc in main_courses:
        dfs(mc)

    # Step 2: Topological sort on subgraph of needed courses
    in_deg = defaultdict(int)
    graph = defaultdict(list)

    for u in needed:
        for v in dependencies[u]:
            if v in needed:
                graph[v].append(u)
                in_deg[u] += 1

    # Step 3: Kahn’s algorithm (BFS-based topological sort)
    queue = deque()
    for u in needed:
        if in_deg[u] == 0:
            queue.append(u)

    result = []
    while queue:
        u = queue.popleft()
        result.append(u)
        for v in graph[u]:
            in_deg[v] -= 1
            if in_deg[v] == 0:
                queue.append(v)

    if len(result) < len(needed):
        print(-1)
    else:
        print(len(result))
        print(' '.join(map(str, result)))

main()
