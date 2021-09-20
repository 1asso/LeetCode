# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root or root == p or root == q:
            return root
        l = self.lowestCommonAncestor(root.left, q, p)
        r = self.lowestCommonAncestor(root.right, q, p)
        if l and r:
            return root
        return l or r