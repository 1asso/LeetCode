# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def traverse(self, root, res):
        if not root:
            return
        self.traverse(root.left, res)
        res.append(root.val)
        self.traverse(root.right, res)

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        res = []
        self.traverse(root, res)
        for i in range(1, len(res)):
            if res[i] <= res[i-1]:
                return False
        return True