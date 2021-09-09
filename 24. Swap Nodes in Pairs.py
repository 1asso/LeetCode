# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy_head = ListNode(next=head)
        pre = dummy_head
        cur = head
        while cur and cur.next:
            tmp = cur.next.next
            pre.next = cur.next
            cur.next.next = cur
            pre = cur
            cur.next = tmp
            cur = tmp
        return dummy_head.next