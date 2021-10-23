# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def midNode(self, head):
        p1, p2 = head, head
        while p2.next and p2.next.next:
            p1, p2 = p1.next, p2.next.next
        return p1
    
    def mergeList(self, l1, l2):
        if not l1 or not l2:
            return l1 or l2
        if l1.val < l2.val:
            l1.next = self.mergeList(l1.next, l2)
            return l1
        else:
            l2.next = self.mergeList(l1, l2.next)
            return l2
        
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        
        mid = self.midNode(head)
        l1, l2 = head, mid.next
        mid.next = None
        
        l1 = self.sortList(l1)
        l2 = self.sortList(l2)
        
        return self.mergeList(l1, l2)
