# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import defaultdict,deque
class Solution:
    def verticalTraversal(self, root) :
        result=[]
        if not root:
            return result
        q=deque([(root,0,0)])
        s=defaultdict(list)
        while q:
            node,row,col=q.popleft()
            if node:
                s[col].append((row,node.val))
                q.append((node.left,row+1,col-1))
                q.append((node.right,row+1,col+1))
        for col in sorted(s.keys()):
            r=sorted(s[col])
            result.append([val for row,val in r])
        return result
                