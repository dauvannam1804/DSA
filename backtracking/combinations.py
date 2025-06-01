def PrintAns(a):
    for i in range(len(a)):
        print(a[i], end=' ')
    print()

def permute(a, l, n, k):
    if k == 0:
        PrintAns(a)
        return
    
    for i in range(l, n + 1):
        a.append(i)
        permute(a, i + 1, n, k - 1)
        a.pop()

if __name__ == "__main__":
    n = 3
    k = 2
    a = []
    permute(a, 1, n, k)