# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        inorder_dict = {v:k for k, v in enumerate(inorder)}
        self.index = 0
        def build(inorder_l, inorder_r):
            if inorder_l > inorder_r:
                return None
            node = TreeNode(preorder[self.index])
            self.index += 1
            i = inorder_dict[node.val]
            node.left = build(inorder_l, i-1)
            node.right = build(i+1, inorder_r)
            return node
        return build(0, len(inorder)-1)