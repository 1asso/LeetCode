Recursion:

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        res = []
        if root.left:
            res += self.postorderTraversal(root.left)
        if root.right:
            res += self.postorderTraversal(root.right)
        res += [root.val, ]
        return res
        

Iteration:

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        res = []
        st = [root]  
        while st:
            node = st.pop()
            if node:
                st += [node, None]
                if node.right:
                    st.append(node.right)
                if node.left:
                    st.append(node.left)
            else:
                res.append(st.pop().val)
        return res