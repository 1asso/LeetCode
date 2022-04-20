# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        queue = collections.deque([(root, 0)])
        max_width = 0
        while queue:
            max_width = max(max_width, queue[-1][1] - queue[0][1] + 1)
            for _ in range(len(queue)):
                node, val = queue.popleft()
                if node.left:
                    queue.append((node.left, val * 2))
                if node.right:
                    queue.append((node.right, val * 2 + 1))
        return max_width