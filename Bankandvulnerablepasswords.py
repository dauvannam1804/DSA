# https://vjudge.net/problem/CodeChef-BANKPASS


class TrieNode:
    def __init__(self) -> None:
        self.child = {}
        self.isEnd = False

class Trie:
    def __init__(self) -> None:
        self.root = TrieNode()

    def insert(self, s):
        currNode: TrieNode = self.root

        for c in s:
            if c not in currNode.child:
                currNode.child[c] = TrieNode()
            currNode = currNode.child[c]
            if currNode.isEnd: return True
        
        if currNode.child: return True
        currNode.isEnd = True
        return False



N = int(input())
trie = Trie()
res = ""
for _ in range(N):
    if trie.insert(input()):
        res = "vulnerable"
        break

if res != "":
    print(res)
else: print("non vulnerable")
'''
2
likemeifyoucan
likeme
'''