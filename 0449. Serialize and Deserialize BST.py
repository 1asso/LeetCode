# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root: Optional[TreeNode]) -> str:
        """Encodes a tree to a single string.
        """
        data = []
        def dfs(node):
            if node:
                data.append(str(node.val))
                dfs(node.left)
                dfs(node.right)
        dfs(root)
        return ' '.join(data)
        
    def deserialize(self, data: str) -> Optional[TreeNode]:
        """Decodes your encoded data to tree.
        """
        data = collections.deque(data.split())
        def dfs(min_val, max_val):
            if data and min_val < int(data[0]) < max_val:
                val = int(data.popleft())
                node = TreeNode(val)
                node.left = dfs(min_val, val)
                node.right = dfs(val, max_val)
                return node
        return dfs(float('-inf'), float('inf'))

        
# Your Codec object will be instantiated and called as such:
# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# tree = ser.serialize(root)
# ans = deser.deserialize(tree)
# return ans