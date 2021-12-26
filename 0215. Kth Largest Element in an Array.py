Priority queue:

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []
        for num in nums:
            heapq.heappush(heap, -num)
        res = None
        for _ in range(k):
            res = -heapq.heappop(heap)
        return res
        

OR:

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = nums[:k]
        heapq.heapify(heap)
        for num in nums[k:]:
            heapq.heappush(heap, num)
            heapq.heappop(heap)
        return heap[0]