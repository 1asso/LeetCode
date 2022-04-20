# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class FindElements:

    def __init__(self, root: Optional[TreeNode]):
        self.root = root
        self.values = set()
        def dfs(node, val):
            if node:
                self.values.add(val)
                node.val = val
                dfs(node.left, val * 2 + 1)
                dfs(node.right, val * 2 + 2)
        dfs(self.root, 0)

    def find(self, target: int) -> bool:
        return target in self.values


# Your FindElements object will be instantiated and called as such:
# obj = FindElements(root)
# param_1 = obj.find(target)