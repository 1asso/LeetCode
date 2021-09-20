# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        def buildList(root, l):
            if not root:
                return
            buildList(root.left, l)
            l.append(root.val)
            buildList(root.right, l)
        l = []
        buildList(root, l)
        d = Counter(l)
        val = max(d.values())
        return [k for k, v in d.items() if v == val]