# https://www.hackerearth.com/problem/algorithm/power-of-2-18/

def max_power_of_two(n):
    print(bin(n))
    print(bin(~n))
    print(bin(~n + 1))
    low = (n & -n)
    print(low)
    print(bin(low))
    print(low.bit_length())
    return (n & -n).bit_length() - 1

# Input
n = int(input())
print(max_power_of_two(n))
