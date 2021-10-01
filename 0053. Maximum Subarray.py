Greedy:

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res, count = float('-inf'), 0
        for i in range(len(nums)):
            count += nums[i]
            if count > res:
                res = count
            if count < 0:
                count = 0
        return res
        

DP:

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        dp = [0] * len(nums)
        dp[0] = nums[0]
        for i in range(1, len(nums)):
            dp[i] = max(nums[i], dp[i-1] + nums[i])
        return max(dp)