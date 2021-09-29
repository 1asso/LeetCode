# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def dfs(self, root):
        if not root:
            return 2
        left = self.dfs(root.left)
        right = self.dfs(root.right)
        if left == 0 or right == 0:
            self.res += 1
            return 1
        elif left == 1 or right == 1:
            return 2
        elif left == 2 and right == 2:
            return 0
    def minCameraCover(self, root: Optional[TreeNode]) -> int:
        self.res = 0
        if self.dfs(root) == 0:
            self.res += 1
        return self.res