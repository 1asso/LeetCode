# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def DFS(self, root, dp):
        if not root:
            return 0
        left = self.DFS(root.left, dp)
        right = self.DFS(root.right, dp)
        dp[root] = max(root.val + left + right, dp[root.left] + dp[root.right])
        return dp[root.left] + dp[root.right]
        
    def rob(self, root: Optional[TreeNode]) -> int:
        dp = {}
        dp[None] = 0
        self.DFS(root, dp)
        return dp[root]
        
        
OR:

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def DFS(self, root):
        if not root:
            return 0, 0  # steal this node, don't steal this node
        left = self.DFS(root.left)
        right = self.DFS(root.right)
        val1 = root.val + left[1] + right[1]
        val2 = max(left[0], left[1]) + max(right[0], right[1])
        return val1, val2
        
    def rob(self, root: Optional[TreeNode]) -> int:
        res = self.DFS(root)
        return max(res)