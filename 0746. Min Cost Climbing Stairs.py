class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp = [0, 0]
        cost.append(0)
        for i in range(2, len(cost)):
            dp.append(min(dp[i-1] + cost[i-1], dp[i-2] + cost[i-2]))
        return dp[-1]
        
        
OR:

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp = cost[:2]
        for i in range(2, len(cost)):
            dp.append(min(dp[i-1], dp[i-2]) + cost[i])
        return min(dp[-1], dp[-2])