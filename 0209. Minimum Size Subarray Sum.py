class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        last = 0
        s = 0
        min_size = len(nums) + 1
        for i in range(len(nums)):
            s += nums[i]
            while s >= target:
                min_size = min(min_size, i-last+1)
                s -= nums[last]
                last += 1
                
        return min_size if min_size <= len(nums) else 0