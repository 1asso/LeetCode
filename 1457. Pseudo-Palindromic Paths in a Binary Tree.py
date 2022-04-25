Use set (High space complexity):

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pseudoPalindromicPaths (self, root: Optional[TreeNode]) -> int:
        count = 0
        def dfs(node, singles):
            nonlocal count
            if not node:
                return
            new = singles.copy()
            if node.val in singles:
                new.remove(node.val)
            else:
                new.add(node.val)
            if not node.left and not node.right:
                count += len(new) <= 1
            dfs(node.left, new)
            dfs(node.right, new)
        dfs(root, set())
        return count
        

Use bit manipulation:

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pseudoPalindromicPaths (self, root: Optional[TreeNode]) -> int:
        count = 0
        def dfs(node, path):
            nonlocal count
            if not node:
                return
            path ^= 1 << node.val
            if not node.left and not node.right:
                count += path & (path - 1) == 0
            dfs(node.left, path)
            dfs(node.right, path)
        dfs(root, 0)
        return count