O(2n):

"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        dummy = Node(0)
        link = {None: None}
        m = n = head
        while m:
            link[m] = Node(m.val)
            m = m.next
        while n:
            link[n].next = link[n.next]
            link[n].random = link[n.random]
            n = n.next
        return link[head]
        
        
O(n):

"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        d = defaultdict(lambda: Node(0))
        d[None] = None
        cur = head
        while cur:
            d[cur].val = cur.val
            d[cur].next = d[cur.next]
            d[cur].random = d[cur.random]
            cur = cur.next
        return d[head]