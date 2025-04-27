# https://codeforces.com/problemset/problem/510/C
from collections import defaultdict, deque
 
def find_alphabet_order(names):
    # Bước 1: Xây đồ thị
    graph = defaultdict(list)
    indegree = {chr(i): 0 for i in range(ord('a'), ord('z')+1)}
    print(indegree)
    n = len(names)
    for i in range(n-1):
        w1 = names[i]
        w2 = names[i+1]
        min_len = min(len(w1), len(w2))
        found_diff = False
        
        for j in range(min_len):
            if w1[j] != w2[j]:
                graph[w1[j]].append(w2[j])
                indegree[w2[j]] += 1
                found_diff = True
                break
        
        # Nếu không tìm thấy khác biệt mà w1 dài hơn w2 => Impossible
        if not found_diff and len(w1) > len(w2):
            return "Impossible"
    
    # Bước 2: Topological sort
    queue = deque()
    for c in indegree:
        if indegree[c] == 0:
            queue.append(c)
    
    result = []
    while queue:
        c = queue.popleft()
        result.append(c)
        for neighbor in graph[c]:
            indegree[neighbor] -= 1
            if indegree[neighbor] == 0:
                queue.append(neighbor)
    
    # Nếu chưa đi qua đủ 26 chữ cái → có chu trình
    if len(result) != 26:
        return "Impossible"
    
    return ''.join(result)
 
# Đọc input
n = int(input())
names = [input().strip() for _ in range(n)]
 
# In kết quả
print(find_alphabet_order(names))