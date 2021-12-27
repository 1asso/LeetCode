Recursion:

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        if not p:
            return not s
        first_match = s and p[0] in [s[0], '.']
        if len(p) >= 2 and p[1] == '*':
            return self.isMatch(s, p[2:]) or (first_match and self.isMatch(s[1:], p))
        else:
            return first_match and self.isMatch(s[1:], p[1:])
            
            
DP:

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        dp = [[False] * (len(p) + 1) for _ in range(len(s) + 1)]
        dp[0][0] = True
        for j in range(2, len(p) + 1):
            dp[0][j] = p[j - 1] == '*' and dp[0][j - 2]
        for i in range(1, len(s) + 1):
            for j in range(1, len(p) + 1):
                if p[j - 1] == '*':
                    if s[i - 1] != p[j - 2] and p[j - 2] != '.':
                        dp[i][j] = dp[i][j - 2]
                    else:
                        dp[i][j] = dp[i - 1][j] or dp[i][j - 1] or dp[i][j - 2]
                else:
                    dp[i][j] = dp[i - 1][j - 1] and p[j - 1] in ['.', s[i - 1]]
        return dp[-1][-1]