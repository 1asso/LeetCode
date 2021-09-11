Iteration:
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        qp, qq = deque([p]), deque([q])   
        while qp and qq:
            if len(qp) != len(qq): 
                return False
            for _ in range(len(qp)):
                n1 = qp.popleft()
                n2 = qq.popleft()
                if (n1 and not n2) or (n2 and not n1): 
                    return False
                if n1 and n2:
                    if n1.val != n2.val:
                        return False
                    else:
                        qp += [n1.left, n1.right]
                        qq += [n2.left, n2.right]
        if len(qp) or len(qq):
            return False
        else:
            return True
            
            
Recursion:
Similar to Q101