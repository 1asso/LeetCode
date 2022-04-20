# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        if depth == 1:
            node = TreeNode(val)
            node.left = root
            return node
            
        def dfs(node, d):
            if not node:
                return node
            if d == depth - 1:
                node.left, node.left.left = TreeNode(val), node.left
                node.right, node.right.right = TreeNode(val), node.right
                return node
            dfs(node.left, d + 1)
            dfs(node.right, d + 1)
            return node
        return dfs(root, 1)