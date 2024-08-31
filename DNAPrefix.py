# https://vjudge.net/problem/LightOJ-1224
# References #49036064 | Mahadi_Irl's solution for [LightOJ-1224] [Problem C]

class TrieNode:
    def __init__(self):
        self.children = [None] * 4
        self.count = 0

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, s):
        curr_node: TrieNode = self.root
        n = len(s)
        for i in range(n):
            x = 0
            if s[i] == "C":
                x = 1
            elif s[i] == "G":
                x = 2
            elif s[i] == "T":
                x = 3
            if curr_node.children[x] is None:
                curr_node.children[x] = TrieNode()
            curr_node = curr_node.children[x]
            curr_node.count += 1
    
    def compute(self, node: TrieNode, level):
        res = node.count * level
        for child in node.children:
            if child is not None:
                res = max(res, self.compute(child, level+1))
        return res
    
    def delete(self, node: TrieNode):
        for child in node.children:
            if child is not None:
                self.delete(child)
        del node

T = int(input())

for i in range(1, T + 1):
    trie = Trie()
    n = int(input())
    for _ in range(n):
        trie.insert(input())
    
    print(f"Case {i}: {trie.compute(trie.root, 0)}")
    trie.delete(trie.root)

'''
3
4
ACGT
ACGTGCGT
ACCGTGC
ACGCCGT
3
CGCGCGCGCGCGCCCCGCCCGCGC
CGCGCGCGCGCGCCCCGCCCGCAC
CGCGCGCGCGCGCCCCGCCCGCTC
2
CGCGCCGCGCGCGCGCGCGC
GGCGCCGCGCGCGCGCGCTC

'''