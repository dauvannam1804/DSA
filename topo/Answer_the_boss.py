# https://www.spoj.com/problems/RPLA/
from collections import defaultdict, deque

def solve_rpla():
    t = int(input())  # Number of test cases
    
    for case in range(1, t + 1):
        n, r = map(int, input().split())  # n = employees, r = relations
        
        # Create graph and track in-degree for each employee
        graph = defaultdict(list)
        in_degree = [0] * n
        
        # Process relations
        for _ in range(r):
            r1, r2 = map(int, input().split())
            # r1 is lower than r2, so r2 -> r1 in our graph
            graph[r2].append(r1)
            in_degree[r1] += 1
        
        # Find employees with in-degree 0 (bosses)
        queue = deque()
        for i in range(n):
            if in_degree[i] == 0:
                queue.append(i)
        
        # Perform topological sort to determine ranks
        ranks = [0] * n
        current_rank = 1
        
        while queue:
            # Process all employees at the current rank
            level_size = len(queue)
            employees_at_level = []
            
            for _ in range(level_size):
                employee = queue.popleft()
                employees_at_level.append(employee)
                
                # Process subordinates
                for subordinate in graph[employee]:
                    in_degree[subordinate] -= 1
                    if in_degree[subordinate] == 0:
                        queue.append(subordinate)
            
            # Sort employees at this level lexicographically
            employees_at_level.sort()
            
            # Assign ranks
            for employee in employees_at_level:
                ranks[employee] = current_rank
            
            current_rank += 1
        
        # Output results
        print(f"Scenario #{case}:")
        
        # Create a list of (rank, employee) pairs and sort them
        result = [(ranks[i], i) for i in range(n)]
        result.sort()  # Sort by rank first, then by employee number
        
        for rank, employee in result:
            print(f"{rank} {employee}")
        
        # Print blank line between test cases if not the last one
        if case < t:
            print()

# Run the solver
solve_rpla()


'''
2
5 6
2 0
2 4
1 4
1 2
3 2
4 0
5 4
1 0
2 0
3 2
4 2
'''