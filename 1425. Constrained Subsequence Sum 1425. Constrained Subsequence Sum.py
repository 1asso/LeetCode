# dp[0] = nums[0]
# dp[i] = max(dp[i - k], dp[i-k+1], ..., dp[i - 1], 0) + x
class Solution:
    def constrainedSubsetSum(self, nums: List[int], k: int) -> int:
        dp = nums[:1]
        maxq = deque(dp) # decreasing
        for i, x in enumerate(nums[1:], 1):
            if i > k and dp[i - k - 1] == maxq[0]:
                maxq.popleft()
            dp.append(max(maxq[0], 0) + x)
            while maxq and dp[i] > maxq[-1]:
                maxq.pop()
            maxq.append(dp[i])
        return max(dp)