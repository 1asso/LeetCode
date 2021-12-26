Divide & Conquer (nlogk, n is the total number of nodes in two lists, k is the number of lists):

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
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []
        dummy = ListNode()
        cur = dummy
        for node in lists:
            if node:
                heappush(heap, (node.val, id(node), node))
        while heap:
            cur.next = heappop(heap)[2]
            cur = cur.next
            if cur.next:
                heappush(heap, (cur.next.val, id(cur.next), cur.next))
        return dummy.next
