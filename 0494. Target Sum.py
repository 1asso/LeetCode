class Solution:    
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        if (sum(nums) + target) % 2 or sum(nums) < abs(target):
            return 0
        target = (sum(nums) + target) // 2
        dp = [0] * (target+1)
        dp[0] = 1
        
        for i in range(len(nums)):
            for j in reversed(range(nums[i], target+1)):
                dp[j] += dp[j-nums[i]]
        return dp[-1]