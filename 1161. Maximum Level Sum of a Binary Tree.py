# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        queue = deque([root])
        max_val, min_depth = float('-inf'), 0
        depth = 0
        while queue:
            s = 0
            depth += 1
            for _ in range(len(queue)):
                node = queue.popleft()
                s += node.val
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            if s > max_val:
                max_val, min_depth = s, depth
        return min_depth