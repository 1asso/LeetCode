DP (bottom-right to top-left) O(mn):

class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        m, n = len(dungeon), len(dungeon[0])
        
        dp = [[float('inf') for _ in range(n + 1)] for _ in range(m + 1)]
        dp[m][n - 1], dp[m - 1][n] = 1, 1
        
        for i in reversed(range(m)):
            for j in reversed(range(n)):
                dp[i][j] = max(min(dp[i + 1][j], dp[i][j + 1]) - dungeon[i][j], 1)
        return dp[0][0]