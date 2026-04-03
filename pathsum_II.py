class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        res = []
        
        def dfs(node, target, path):
            if not node:
                return
            
            # current node ko path me add karo
            path.append(node.val)
            
            # leaf node check
            if not node.left and not node.right and target - node.val == 0:
                res.append(path.copy())   # important
                
            # left and right recursion
            if node.left:
                dfs(node.left, target - node.val, path)
            if node.right:
                dfs(node.right, target - node.val, path)
            
            # backtracking
            path.pop()
        
        dfs(root, targetSum, [])
        return res