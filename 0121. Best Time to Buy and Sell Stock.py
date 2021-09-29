Greedy:

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_p = 10000
        profit = 0
        for p in prices:
            min_p = min(p, min_p)
            profit = max(profit, p - min_p)
        return profit
        

DP:

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = [[0, 0]] * len(prices)
        dp[0] = [-prices[0], 0]
        # dp[i] = [max balance when holding a stock, max balance when not holding a stock]
        for i in range(1, len(prices)):
            dp[i] = [max(-prices[i], dp[i-1][0]), \
                     max(dp[i-1][1], dp[i-1][0] + prices[i])]
        return max(dp[-1])