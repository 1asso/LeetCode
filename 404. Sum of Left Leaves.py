Recursion:

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:    
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        l_sum = self.sumOfLeftLeaves(root.left)
        r_sum = self.sumOfLeftLeaves(root.right)
        if root.left and not root.left.left and not root.left.right:
            return root.left.val + l_sum + r_sum
        else:
            return l_sum + r_sum


Iteration:

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:    
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        q = deque([root])
        res = 0
        while q:
            for _ in range(len(q)):
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                    if not node.left.left and not node.left.right:
                        res += node.left.val
                if node.right:
                    q.append(node.right)
        return res  