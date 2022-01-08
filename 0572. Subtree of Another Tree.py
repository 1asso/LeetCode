Recursion O(|S|*|T|):

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isMatch(self, t, s):
        if not (t and s):
            return t == s
        return (t.val == s.val) and self.isMatch(t.left, s.left) \
            and self.isMatch(t.right, s.right)
    
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if self.isMatch(root, subRoot):
            return True
        elif not root:
            return False
        else:
            return self.isSubtree(root.left, subRoot) \
                or self.isSubtree(root.right, subRoot)
                
                
Merkle Hashing O(|S|+|T|):

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def merkle(self, node):
        if not node:
            return '#'
        l = self.merkle(node.left)
        r = self.merkle(node.right)
        node.merkle = str(hash(l + str(node.val) + r))
        return node.merkle
    
    def dfs(self, node, val):
        if not node:
            return False
        return node.merkle == val or \
            self.dfs(node.left, val) or self.dfs(node.right, val)
    
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        self.merkle(root)
        self.merkle(subRoot)
        return self.dfs(root, subRoot.merkle)