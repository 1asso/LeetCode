# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        queue_o = deque([original])
        queue_c = deque([cloned])
        while queue_o:
            node_o = queue_o.popleft()
            node_c = queue_c.popleft()
            if node_o == target:
                return node_c
            if node_o:
                queue_o.extend([node_o.left, node_o.right])
                queue_c.extend([node_c.left, node_c.right])