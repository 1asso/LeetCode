# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        def buildList(root, l):
            if not root:
                return
            buildList(root.left, l)
            l.append(root.val)
            buildList(root.right, l)
        l = []
        res = float('inf')
        buildList(root, l)
        for i in range(1, len(l)):
            res = min(abs(l[i] - l[i-1]), res)
        return res