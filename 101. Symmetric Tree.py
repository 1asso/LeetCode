Iteration:

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        q = deque([root])
        while q:
            res = []
            for _ in range(len(q)):
                node = q.popleft()
                if node:
                    q += [node.left, node.right]
                    res.append(node.val)
                else:
                    res.append(None)
            if res != res[::-1]:
                return False
        return True
        
        
Recursion:

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        
        def compare(left, right):
            if (left and not right) or (right and not left):
                return False
            elif not left and not right:
                return True
            elif left.val != right.val:
                return False
            else:
                outside = compare(left.left, right.right)
                inside = compare(left.right, right.left)
                return inside and outside
            
        return compare(root.left, root.right)