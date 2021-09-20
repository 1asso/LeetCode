# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        def construct(nums):
            if not nums:
                return None
            node = TreeNode(max(nums))
            i = nums.index(node.val)
            node.left = construct(nums[:i])
            node.right = construct(nums[i+1:])
            return node
        return construct(nums)