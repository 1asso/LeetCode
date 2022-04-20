# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        depth = {}
        def dfs(node, d):
            if node:
                depth[node] = d
                dfs(node.left, d + 1)
                dfs(node.right, d + 1)
        dfs(root, 0)
        max_depth = max(depth.values())
        
        def lca(node):
            if not node:
                return None
            l, r = lca(node.left), lca(node.right)
            if depth[node] == max_depth or l and r:
                return node
            return l or r
        return lca(root)