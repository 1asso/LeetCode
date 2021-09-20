# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        self.pre = 0
        def build(root):
            if not root:
                return None
            build(root.right)
            root.val += self.pre
            self.pre = root.val
            build(root.left)
        build(root)
        return root