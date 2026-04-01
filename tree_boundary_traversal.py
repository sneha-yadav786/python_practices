'''
class Node:
    def __init__(self, val):
        self.data = val
        self.right = None
        self.left = None
'''

class Solution:
    def boundaryTraversal(self, root):
        res = []
        if not root:
            return res
        def isLeaf(node):
            return not node.left and not node.right
        if not isLeaf(root):
            res.append(root.data)
        curr = root.left
        while curr:
            if not isLeaf(curr):
                res.append(curr.data)
            if curr.left:
                curr = curr.left
            else:
                curr = curr.right
        def addLeaves(node):
            if not node:
                return
            if isLeaf(node):
                res.append(node.data)
                return
            addLeaves(node.left)
            addLeaves(node.right)
        addLeaves(root)
        curr = root.right
        temp = []
        while curr:
            if not isLeaf(curr):
                temp.append(curr.data)
            if curr.right:
                curr = curr.right
            else:
                curr = curr.left
        res.extend(temp[::-1])
        return res
        
        