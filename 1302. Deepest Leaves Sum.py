# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        queue = [root]
        while queue:
            prev, queue = queue, [child for node in queue for child in [node.left, node.right] if child]
        return sum(node.val for node in prev)