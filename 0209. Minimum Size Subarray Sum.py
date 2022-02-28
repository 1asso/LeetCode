class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        i, s, res = 0, 0, len(nums) + 1
        for j in range(len(nums)):
            s += nums[j]
            while s >= target:
                res = min(res, j - i + 1)
                s -= nums[i]
                i += 1
        return res if res < len(nums) + 1 else 0