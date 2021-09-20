Iteration:

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        cur = root
        parent = None, None
        while cur:
            if key < cur.val:
                parent = cur, 0
                cur = cur.left
            elif key > cur.val:
                parent = cur, 1
                cur = cur.right
            elif key == cur.val:
                if cur.left and cur.right:
                    l = cur.left
                    r = cur.right
                    node = r
                    while r.left:
                        r = r.left
                    r.left = l
                elif not cur.left and not cur.right:
                    node = None
                else:
                    node = cur.left or cur.right
                if not parent[0]:
                    return node
                elif parent[1]:
                    parent[0].right = node
                else:
                    parent[0].left = node
                break
        return root


Recursion:

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return None
        if key == root.val:
            if root.left and root.right:
                l = root.left
                r = root.right
                while r.left:
                    r = r.left
                r.left = l
                return root.right
            elif not root.left and not root.right:
                return None
            else:
                return root.left or root.right
        if key < root.val:
            root.left = self.deleteNode(root.left, key)
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
        return root