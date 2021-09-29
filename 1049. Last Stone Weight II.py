0-1 knapsack:

class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        target = sum(stones) // 2
        dp = [0] * (target+1)
        for i in range(len(stones)):
            for j in reversed(range(stones[i], target+1)):
                dp[j] = max(dp[j], dp[j-stones[i]] + stones[i])
        return sum(stones) - 2 * dp[-1]
        
        
DFS:

class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        target = ceil(sum(stones) / 2)

        @cache # works when all arguments are hashable
        def dp(i, s):
            if s < 0: return False
            if s == 0: return True
            if i == 0: return s == stones[0]
            return dp(i-1, s) or dp(i-1, s-stones[i])

        max_sum = None
        for s in range(target, -1, -1):
            if dp(len(stones)-1, s):
                max_sum = s
                break

        return abs(sum(stones) - 2 * max_sum)