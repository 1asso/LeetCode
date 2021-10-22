Divide & Conquer:

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None
        if len(lists) == 1:
            return lists[0]
        mid = len(lists) // 2
        l, r = self.mergeKLists(lists[:mid]), self.mergeKLists(lists[mid:])
        return self.merge(l, r)
    
    def merge(self, l, r):
        if not l or not r:
            return l or r
        if l.val < r.val:
            l.next = self.merge(l.next, r)
            return l
        r.next = self.merge(l, r.next)
        return r
        
        
Priority Queue:

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

import queue

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        q = queue.PriorityQueue()
        dummy = ListNode()
        cur = dummy
        for node in lists:
            if node:
                q.put((node.val, id(node), node))
        while q.qsize():
            cur.next = q.get()[2]
            cur = cur.next
            if cur.next:
                q.put((cur.next.val, id(cur.next), cur.next))
        return dummy.next