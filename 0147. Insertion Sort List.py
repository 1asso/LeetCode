# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy_head, cur = ListNode(val=-5001), head
        while cur:
            cand, cur, tmp = cur, cur.next, dummy_head
            while tmp:
                if cand.val >= tmp.val and (not tmp.next or cand.val < tmp.next.val):
                    cand.next, tmp.next = tmp.next, cand
                    break
                tmp = tmp.next
        return dummy_head.next