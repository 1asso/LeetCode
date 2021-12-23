Brute Force:

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        for i in range(len(prices)-1):
            res += max(prices[i+1] - prices[i], 0)
        return res
        
        
Greedy:

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        profit = 0
        for i in range(1, len(prices)):
            if prices[i] >= prices[i-1]:
                profit += prices[i] - prices[i-1]
            else:
                res += profit
                profit = 0
        res += profit
        return res
        
        
DP:

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = [[0, 0] for _ in range(len(prices))]
        dp[0] = [-prices[0], 0]  # holding, not holding a stock
        for i in range(1, len(prices)):
            dp[i][0] = max(dp[i-1][1] - prices[i], dp[i-1][0])
            dp[i][1] = max(dp[i-1][0] + prices[i], dp[i-1][1])
        return dp[-1][1]