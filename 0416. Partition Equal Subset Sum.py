0-1 knapsack:

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        s = sum(nums)
        if s % 2: return False
        l = s // 2
        dp = [0] * (l+1)
        for i in range(len(nums)):
            for j in reversed(range(nums[i], l+1)):
                dp[j] = max(dp[j], dp[j-nums[i]] + nums[i])
        return dp[-1] == l
        
        
        
OR (Backtracking):

class Solution:
    def backtracking(self, nums, target, cache):
        if target == 0:
            return True
        if target < 0:
            return False
        if target in cache:
            return False
        cache.add(target)
        for i in range(len(nums)):
            if self.backtracking(nums[i+1:], target-nums[i], cache):
                return True
        return False
    
    def canPartition(self, nums: List[int]) -> bool:
        return not sum(nums) % 2 and self.backtracking(nums, sum(nums)//2, set())