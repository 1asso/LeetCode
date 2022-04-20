# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        res = 0
        # p: if parent is even
        # g: if grandparent is even
        def dfs(node, p, g):
            nonlocal res
            if not node:
                return
            if g:
                res += node.val
            dfs(node.left, not node.val % 2, p)
            dfs(node.right, not node.val % 2, p)
            
        dfs(root, False, False)
        return res