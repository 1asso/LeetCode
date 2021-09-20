Recursion:

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        res = []
        if root.left:
            res += self.inorderTraversal(root.left)
        res += [root.val]
        if root.right:
            res += self.inorderTraversal(root.right)
        return res
        

Iteration:

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        st = [root]
        res = []
        while st:
            node = st.pop()
            if node:
                if node.right:
                    st.append(node.right)
                st += [node, None]
                if node.left:
                    st.append(node.left)
            else:
                res.append(st.pop().val)
        return res