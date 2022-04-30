"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        queue = deque([root])
        while queue:
            l = len(queue)
            for i in range(l):
                cur = queue.popleft()
                if cur:
                    if i < l - 1:
                        cur.next = queue[0]
                    else:
                        cur.next = None
                    queue.extend([cur.left, cur.right])
        return root