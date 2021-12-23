Greedy:

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        cur_sum, max_sum = 0, float('-inf')
        for i in range(len(nums)):
            cur_sum += nums[i]
            max_sum = max(max_sum, cur_sum)
            if cur_sum < 0:
                cur_sum = 0
        return max_sum
        

DP:

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        dp = [0] * len(nums)
        dp[0] = nums[0]
        for i in range(1, len(nums)):
            dp[i] = max(nums[i], dp[i-1] + nums[i])
        return max(dp)