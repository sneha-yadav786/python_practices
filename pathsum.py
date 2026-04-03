class Solution:
    def hasPathSum(self, root, targetSum):
        if not root:
            return False
        if not root.left and not root.right:
            return targetSum-root.val==0
        a=False
        b=False
        if root.left:
            a=self.hasPathSum(root.left,targetSum-root.val)
        if root.right:
            b= self.hasPathSum(root.right,targetSum-root.val)
        return a or b
        