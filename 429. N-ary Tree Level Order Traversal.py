"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if not root:
            return []
        q, res = [root], []
        while q:
            res.append([n.val for n in q])
            q = [c for n in q for c in n.children]
        return res
    
OR:
 
"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if not root:
            return []
        res = []
        q = deque([root])
        while q:
            cur_res = []
            for _ in range(len(q)):
                node = q.popleft()
                cur_res.append(node.val)
                for c in node.children:
                    q.append(c)
            res.append(cur_res)
        return res