# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(node, upper, lower):
            if not node:
                return True
            
            if not (lower < node.val < upper):
                return False
            
            return dfs(node.left, node.val, lower) and dfs(node.right, upper, node.val)
        
        return dfs(root, float('inf'), float('-inf'))