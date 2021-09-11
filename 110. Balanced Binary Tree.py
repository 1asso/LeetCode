# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getDepth(self, node):
        if not node:
            return 0
        l_depth = self.getDepth(node.left)
        r_depth = self.getDepth(node.right)
        if l_depth == -1 or r_depth == -1 or abs(l_depth - r_depth) > 1:
            return -1
        else:
            return max(l_depth, r_depth) + 1
    
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        return self.getDepth(root) != -1