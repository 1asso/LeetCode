 # https://leetcode.com/problems/binary-tree-maximum-path-sum/discuss/603423/Python-Recursion-stack-thinking-process-diagram
 
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        max_path = float('-inf')
        def get_max_gain(node):
            nonlocal max_path
            if not node:
                return 0
            left_gain = max(get_max_gain(node.left), 0)
            right_gain = max(get_max_gain(node.right), 0)
            cur_max = node.val + left_gain + right_gain
            max_path = max(max_path, cur_max)
            return node.val + max(left_gain, right_gain)
        get_max_gain(root)
        return max_path