class TrieNode:
    def __init__(self):
        self.children = {}
        self.count = 0

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word, weight):
        node: TrieNode = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
            node.count = max(node.count, weight)
    
    def search(self, prefix):
        node = self.root
        for char in prefix:
            if char not in node.children:
                return -1
            node = node.children[char]
        return node.count

# Read input
n, q = map(int, input().split())

# Create a Trie instance
trie = Trie()

# Insert words into the Trie
for _ in range(n):
    line = list(input().split())
    word = line[0]
    weight = int(line[1])
    trie.insert(word, weight)

# Process queries
for _ in range(q):
    prefix = input().strip()
    print(trie.search(prefix))
