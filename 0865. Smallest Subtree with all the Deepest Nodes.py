See Q236 (2 passes):

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def subtreeWithAllDeepest(self, root: TreeNode) -> TreeNode:
        depth = {None: -1}
        
        def dfs(node, parent=None):
            if node:
                depth[node] = depth[parent] + 1
                dfs(node.left, node)
                dfs(node.right, node)
        dfs(root)
        
        max_depth = max(depth.values())
        
        def findLowestCommonAncestor(node):
            if not node:
                return None
            l = findLowestCommonAncestor(node.left)
            r = findLowestCommonAncestor(node.right)
            if depth[node] == max_depth or (l and r):
                return node
            return l or r
        
        return findLowestCommonAncestor(root)