# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def same(q, p):
            if not q and not p :
                return True
            
            if (not q and p) or (q and not p):
                return False
            
            if q.val != p.val:
                return False
            
            return same(q.left, p.left) and same(q.right, p.right)
        
        def has_subtree(root, subroot):
            if not root:
                return False
            
            if same(root, subroot):
                return True
            
            return has_subtree(root.left, subroot) or has_subtree(root.right, subroot)
        
        return has_subtree(root, subRoot)