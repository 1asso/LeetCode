Recursion:

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        res = [root.val, ]
        if root.left:
            res += self.preorderTraversal(root.left)
        if root.right:
            res += self.preorderTraversal(root.right)
        return res
        
        
Iteration:

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        res = []
        st = [root]
        while st:
            node = st.pop()
            if node:
                if node.right: 
                    st.append(node.right)
                if node.left:
                    st.append(node.left)
                st += [node, None]
            else:
                res.append(st.pop().val)
        return res

