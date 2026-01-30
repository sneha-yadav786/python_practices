class Solution:
    def check(self,n1,n2):
        if not n1 and not n2:
            return True
        if not n1 or not n2:
            return False
        return n1.val==n2.val and self.check(n1.left,n2.right) and self.check(n1.right,n2.left)
    def isSymmetric(self, root) -> bool:
        return self.check(root.left,root.right)
         