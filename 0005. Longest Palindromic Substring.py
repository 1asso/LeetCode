Expand around center:

class Solution:
    def palindromeAt(self, s: str, l: int, r: int) -> str:
        while l >= 0 and r < len(s) and s[l] == s[r]:
            l -= 1
            r += 1
        return s[l+1:r]
    
    def longestPalindrome(self, s: str) -> str:
        longest = ''
        for i in range(len(s)):
            longest = max(self.palindromeAt(s, i, i), \
                          self.palindromeAt(s, i, i+1), longest, key=len)
        return longest
        

DP:

class Solution:
    def longestPalindrome(self, s: str) -> str:
        longest_palindrome = s[0]
        dp = [[0] * len(s) for _ in range(len(s))]
        for i in range(len(s)):
            dp[i][i] = 1
        for i in reversed(range(len(s))):
            for j in range(i+1, len(s)):
                if s[i] == s[j]:
                    if j == i + 1 or dp[i+1][j-1]:
                        dp[i][j] = 1
                        if j + 1 - i > len(longest_palindrome):
                            longest_palindrome = s[i:j+1]
        return longest_palindrome