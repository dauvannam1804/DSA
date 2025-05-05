# https://www.hackerearth.com/practice/basic-programming/bit-manipulation/basics-of-bit-manipulation/practice-problems/algorithm/samu-and-her-birthday-party-1/

def count_min_dishes(n, k, friend_likes):
    friend_masks = []
    for like in friend_likes:
        mask = 0
        for i, c in enumerate(like):
            if c == '1':
                mask |= (1 << i)
        friend_masks.append(mask)

    min_dish_count = k  # tối đa K món
    for subset in range(1, 1 << k):  # duyệt tất cả các tập món ăn
        valid = True
        for friend_mask in friend_masks:
            if (friend_mask & subset) == 0:
                valid = False
                break
        if valid:
            dish_count = bin(subset).count('1')
            min_dish_count = min(min_dish_count, dish_count)
    return min_dish_count

T = int(input())
for _ in range(T):
    n, k = map(int, input().split())
    friend_likes = [input().strip() for _ in range(n)]
    print(count_min_dishes(n, k, friend_likes))


""" 
1
2 2
10 
01
"""