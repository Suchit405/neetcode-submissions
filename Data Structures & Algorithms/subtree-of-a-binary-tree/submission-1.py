# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def issame(p, q):
            if p is None and q is None:
                return True
            if p is None and q:
                return False
            if p and q is None:
                return False
            if p.val != q.val:
                return False
            return issame(p.right, q.right) and issame(p.left, q.left)
        if subRoot is None:
            return True
        if not root:
            return False
        if root.val == subRoot.val and issame(root, subRoot):
            return True
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)