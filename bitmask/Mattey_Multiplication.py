# https://www.hackerearth.com/practice/basic-programming/bit-manipulation/basics-of-bit-manipulation/practice-problems/algorithm/mattey-multiplication-6/

def multiply_with_shifts(n, m):
    shifts = []
    i = 0
    while m > 0:
        if m & 1:
            shifts.append(i)
        i += 1
        m >>= 1
    shifts.sort(reverse=True)
    return ' + '.join(f'({n}<<{k})' for k in shifts)

T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    print(multiply_with_shifts(N, M))


