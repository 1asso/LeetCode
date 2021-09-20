# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def traverse(self, node, res, path):
        path.append(node.val)
        if node.left:
            self.traverse(node.left, res, path)
            path.pop()
        if node.right:
            self.traverse(node.right, res, path)
            path.pop()
        if not node.left and not node.right:
            res.append(sum(path))
            
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        res = []
        self.traverse(root, res, [])
        return targetSum in res


In short:

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:            
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        if not root.left and not root.right and root.val == targetSum:
            return True
        return self.hasPathSum(root.left, targetSum-root.val) \
            or self.hasPathSum(root.right, targetSum-root.val)