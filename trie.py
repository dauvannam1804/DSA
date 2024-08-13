class Node:
    def __init__(self):
        self.countWord = 0
        self.child = dict()

def addWord(root: Node, s):
    temp = root
    for ch in s:
        if ch not in temp.child:
            temp.child[ch] = Node()
        temp = temp.child[ch]
    temp.countWord += 1

def findWord(root: Node, s):
    temp = root
    for ch in s:
        if ch not in temp.child:
            return False
        temp = temp.child[ch]
    return temp.countWord 

def isWord(node: Node):
    return node.countWord != 0

def isEmpty(node: Node):
    return len(node.child) == 0

def removeWord(root: Node, s, level, len):
    if root == None:
        return False
    if level == len:
        if root.countWord > 0:
            root.countWord -= 1
            return True
        return False
    ch = s[level]
    if ch not in root.child:
        return False
    flag = removeWord(root.child[ch], s, level + 1, len)
    if flag == True and isWord(root.child[ch]) == False and \
    isEmpty(root.child[ch]) == True:
        del root.child[ch]
    return flag

def printWord(root: Node, s):
    if isWord(root):
        print(s)
    for ch in root.child:
        printWord(root.child[ch], s + ch)


if __name__ == '__main__':
    root = Node()
    addWord(root, "the")
    printWord(root, "the")
    addWord(root, "then")
    printWord(root, "then")
    addWord(root, "bigo")
    printWord(root, "bigo")
    print(findWord(root, "there"))
    print(findWord(root, "th"))
    print(findWord(root, "the"))
    removeWord(root, "bigo", 0, 4)
    removeWord(root, "the", 0, 3)
    removeWord(root, "then", 0, 4)
    printWord(root, "the")
