Use hashset:

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        visited = set()
        cur = head
        while cur:
            if cur in visited:
                return cur            
            visited.add(cur)
            cur = cur.next
        return None
        
        
Floyd’s Cycle Detection Algorithm:

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        fast = slow = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                p1 = fast
                p2 = head
                while p1 != p2:
                    p1 = p1.next
                    p2 = p2.next
                return p1
        return None
