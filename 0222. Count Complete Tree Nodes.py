# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        l = root.left
        r = root.right
        left_height, right_height = 0, 0
        while l:
            left_height += 1
            l = l.left
        while r:
            right_height += 1
            r = r.right
        if left_height == right_height:
            return (2 << left_height) - 1
        else:
            return 1 + self.countNodes(root.left) + self.countNodes(root.right)