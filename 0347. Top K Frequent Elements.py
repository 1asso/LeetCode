class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if k == len(nums):
            return nums
        count = Counter(nums)
        return heapq.nlargest(k, count.keys(), key=count.get)
        
OR:

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if k == len(nums):
            return nums
        count = Counter(nums)
        heap = []
        for kk, v in count.items():
            heapq.heappush(heap, (v, kk))
            if len(heap) > k:
                heapq.heappop(heap)
        return [y for x, y in heap]