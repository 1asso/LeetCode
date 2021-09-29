class Solution:            
    def climbStairs(self, n: int) -> int:
        dp = [0, 1, 2]
        for i in range(3, n+1):
            dp.append(dp[i-1] + dp[i-2])
        return dp[n]
                

OR m steps:

class Solution:            
    def climb(self, n, m):
        dp = [0, 1, 2]
        for i in range(3, n+1):
            dp.append(0)
            for j in range(1, m+1):
                if i >= j:
                    dp[i] += dp[i-j]
        return dp[n]
    
    def climbStairs(self, n: int) -> int:
        return self.climb(n, 2)
        

Unbounded Knapsack (permutation):

class Solution:            
    def climbStairs(self, n: int) -> int:
        steps = [1, 2]
        dp = [0] * (n + 1)
        dp[0] = 1
        for j in range(n+1):
            for s in steps:
                if j >= s:
                    dp[j] += dp[j-s]
        return dp[-1]