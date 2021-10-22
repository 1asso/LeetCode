O(nlogn):

class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        nums.sort()
        m = 0
        for i in range(1, len(nums)):
            m = max(m, nums[i]-nums[i-1])
        return m
        
        
Bucket Sort:

class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        lo, hi, n = min(nums), max(nums), len(nums)
        if lo == hi:
            return 0
        buckets = defaultdict(list)
        for num in nums:
            ind = (num - lo) * n // (hi - lo) if num != hi else n - 1
            buckets[ind].append(num)
        res = []
        for i in range(n):
            if buckets[i]:
                res.append([min(buckets[i]), max(buckets[i])])
        return max([y[0] - x[1] for x, y in zip(res, res[1:])])
        

Radix Sort:

