Bad:

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if not postorder:
            return None
        mid = postorder[-1]
        root = TreeNode(mid)
        i = inorder.index(mid)
        root.left = self.buildTree(inorder[:i], postorder[:i])
        root.right = self.buildTree(inorder[i+1:], postorder[i:-1])
        return root
        
        
Improved:

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        inorder_dict = {inorder[i]: i for i in range(len(inorder))}
        def construct(in_low, in_high, post_low, post_high):
            node = TreeNode(postorder[post_high])
            if in_low > in_high:
                return None
            i = inorder_dict[node.val]
            i_delta = i - in_low # length of the left subtree
            node.left = construct(in_low, i-1, post_low, i_delta+post_low-1)
            node.right = construct(i+1, in_high, post_low+i_delta, post_high-1)
            return node
        return construct(0, len(inorder)-1, 0, len(inorder)-1)
        

Faster:

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        inorder_dict = {v:i for i, v in enumerate(inorder)}
        self.index = 1
        def construct(in_low, in_high):
            if in_low > in_high:
                return None
            node = TreeNode(postorder[-self.index])
            self.index += 1
            i = inorder_dict[node.val]
            node.right = construct(i+1, in_high)
            node.left = construct(in_low, i-1)
            return node
        return construct(0, len(inorder)-1)