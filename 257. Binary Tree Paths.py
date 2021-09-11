Pass Ref:
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:    
    def traverse(self, node, results, path):
        path.append(str(node.val))
        if node.left:
            self.traverse(node.left, results, path)
            path.pop()
        if node.right:
            self.traverse(node.right, results, path)
            path.pop()
        if not node.left and not node.right:
            results.append('->'.join(path))
            
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        if not root:
            return []
        results = []
        self.traverse(root, results, [])
        return results


Pass Value:
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def traverse(self, node, results, path):
        path.append(str(node.val))
        if node.left:
            self.traverse(node.left, results, path + [])
        if node.right:
            self.traverse(node.right, results, path + [])
        if not node.left and not node.right:
            results.append('->'.join(path))
        
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        if not root:
            return []
        results = []
        self.traverse(root, results, [])
        return results
        