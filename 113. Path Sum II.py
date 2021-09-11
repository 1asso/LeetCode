# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def traverse(self, node, res, path, target):
        path.append(node.val)
        if node.left:
            self.traverse(node.left, res, path+[], target)
        if node.right:
            self.traverse(node.right, res, path+[], target)
        if not node.left and not node.right and sum(path) == target:
            res.append(path)
            
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        res = []
        if not root:
            return res
        self.traverse(root, res, [], targetSum)
        return res