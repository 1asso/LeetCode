Binary Search O(nlogn):
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        def construct(lo, hi):
            if lo >= hi:
                return None
            node = TreeNode(preorder[lo])
            lo += 1
            mid = bisect.bisect_left(preorder, node.val, lo, hi)
            node.left = construct(lo, mid)
            node.right = construct(mid, hi)
            return node
        return construct(0, len(preorder))
        

O(n):        
# https://leetcode.com/problems/construct-binary-search-tree-from-preorder-traversal/discuss/252232/JavaC%2B%2BPython-O(N)-Solution

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        return self.buildTree(preorder[::-1], float('inf'))

    def buildTree(self, preorder, bound):
        if not preorder or preorder[-1] > bound: return None
        node = TreeNode(preorder.pop())
        node.left = self.buildTree(preorder, node.val)
        node.right = self.buildTree(preorder, bound)
        return node