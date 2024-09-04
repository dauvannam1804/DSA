# https://vjudge.net/problem/Kattis-phonelist

class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, number):
        current_node = self.root
        for digit in number:
            if digit not in current_node.children:
                current_node.children[digit] = TrieNode()
            current_node = current_node.children[digit]
            
            # Nếu đã là end of word trước đó, có nghĩa là đã có một số là prefix của số này
            if current_node.is_end_of_word:
                return False
        
        # Nếu đã có con, nghĩa là số này là prefix của số khác
        if current_node.children:
            return False
        
        current_node.is_end_of_word = True
        return True

def is_consistent(phone_list):
    trie = Trie()
    for number in phone_list:
        if not trie.insert(number):
            return False
    return True

# Đọc input
import sys
input = sys.stdin.read
data = input().splitlines()

# Số bộ test
t = int(data[0])
index = 1
for _ in range(t):
    n = int(data[index])
    phone_list = data[index + 1:index + 1 + n]
    index += n + 1
    
    if is_consistent(phone_list):
        print("YES")
    else:
        print("NO")

'''
# INPUT
2
3
911
97625999
91125426
5
113
12340
123440
12345
98346

# OUPUT
NO
YES

'''