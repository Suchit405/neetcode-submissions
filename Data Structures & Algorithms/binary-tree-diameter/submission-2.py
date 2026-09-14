# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        res = 0 #res = max(res, left height + right height) on every node
        def dfs(root):
            nonlocal res #Use nonlocal to modify nonlocal variable
            if not root:
                return 0
            left = dfs(root.left)
            right = dfs(root.right)
            res = max(res, left + right) #This will now check all the diameteres for all the nodes in the tree
            return 1 + max(left , right) # while this will return the height
        dfs(root)
        return res