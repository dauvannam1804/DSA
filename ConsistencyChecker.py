# https://vjudge.net/problem/LightOJ-1129

class TrieNode:
    def __init__(self):
        self.child = [None] * 10
        self.isEnd = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, s):
        currNode = self.root
        n = len(s)

        for i in range(n):
            x = int(s[i]) - 1
            if currNode.child[x] is None:
                currNode.child[x] = TrieNode()
            currNode = currNode.child[x]
        
        currNode.isEnd = True
    
    def check_prefix(self, node: TrieNode):
        for i in range(10):
            if node.child[i] is not None:
                if node.isEnd: return True
                if self.check_prefix(node.child[i]): return True
        return False
    
    def delele(self, node: TrieNode):
        for i in range(10):
            if node.child[i] is not None:
                self.delele(node.child[i])
        
        del node
    
T = int(input())
res = ""
for i in range(1, T + 1):
    n = int(input())
    trie = Trie()
    for _ in range(n):
        trie.insert(input().strip())
    if trie.check_prefix(trie.root):
        res+=f"Case {i}: NO\n" 
    else:
        res+=f"Case {i}: YES\n"
    trie.delele(trie.root)
print(res)

'''
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
'''