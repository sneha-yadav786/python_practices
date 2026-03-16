class Solution:
    def rightSideView(self, root):
        result = []
        
        def dfs(node, level):
            if not node:
                return
            
            # first node at this level
            if level == len(result):
                result.append(node.data)
            
            # go right first
            dfs(node.right, level + 1)
            dfs(node.left, level + 1)
        
        dfs(root, 0)
        return result