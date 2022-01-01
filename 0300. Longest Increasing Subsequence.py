Patience Sorting O(nlogn):

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        piles = []
        for num in nums:
            idx = bisect_left(piles, num)
            if idx == len(piles):
                piles.append(num)            
            else:
                piles[idx] = num
        return len(piles)


DP O(n^2):

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [1] * len(nums)
        for i in range(1, len(nums)):
            for j in range(0, i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[j] + 1, dp[i])
        return max(dp)