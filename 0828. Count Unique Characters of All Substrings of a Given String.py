DP (https://leetcode.com/problems/count-unique-characters-of-all-substrings-of-a-given-string/discuss/1651064/1D-DP-Approach):

class Solution:
    def uniqueLetterString(self, s: str) -> int:
        index, dp = {}, [0] * len(s)
        for i, c in enumerate(s):
            j, k = index.get(c, [-1, -1])
            dp[i] = dp[i - 1] + (i - j) - (j - k)
            index[c] = [i, j]
        return sum(dp)