# https://www.hackerrank.com/challenges/contacts/

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'contacts' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts 2D_STRING_ARRAY queries as parameter.
#

class TrieNode:
    def __init__(self) -> None:
        self.child = [None] * 26  
        self.count = 0

class Trie:
    def __init__(self) -> None:
        self.root = TrieNode()

    def insert(self, s):
        curr_node: TrieNode = self.root
        n = len(s)

        for i in range(n):
            x = ord(s[i]) - 97
            if curr_node.child[x] is None:
                curr_node.child[x] = TrieNode()
            curr_node = curr_node.child[x]
            curr_node.count += 1

    def search(self, s):
        curr_node = self.root
        n = len(s)
        
        for i in range(n):
            x = ord(s[i]) - 97
            if curr_node.child[x] is None:
                return 0
            curr_node = curr_node.child[x]

        return curr_node.count


def contacts(queries):
    res = []
    trie = Trie()
    for q in queries:
        operation, text = q 
        if operation == "add":
            trie.insert(text)
        else:
            res.append(trie.search(text))
    return res
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    queries_rows = int(input().strip())

    queries = []

    for _ in range(queries_rows):
        queries.append(input().rstrip().split())

    result = contacts(queries)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
