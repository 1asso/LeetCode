Iteration:

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        queue = deque([root])
        res = []
        while queue:
            size = len(queue)
            cur_res = []
            for _ in range(size):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                cur_res.append(node.val)
            res.append(cur_res)
        return res
        

Recursion:

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []   
        def compute(node, depth):
            if not node:
                return []
            if len(res) == depth:
                res.append([])
            res[depth].append(node.val)
            if node.left:
                compute(node.left, depth+1)
            if node.right:
                compute(node.right, depth+1)
        compute(root, 0)
        return res