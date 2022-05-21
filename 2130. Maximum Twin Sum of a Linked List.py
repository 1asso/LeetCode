O(N):

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        max_sum = 0
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        cur, prev = slow, None
        while cur:
            cur.next, prev, cur = prev, cur, cur.next
        while prev:
            max_sum = max(max_sum, head.val + prev.val)
            head, prev = head.next, prev.next
        return max_sum