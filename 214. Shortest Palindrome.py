KMP O(N):

class Solution:
    def shortestPalindrome(self, s: str) -> str:
        new_s = s + '*' + s[::-1]
        next = [0, 0]
        j = 0
        for i in range(1, len(new_s)):
            if j > 0 and new_s[i] != new_s[j]:
                j = next[j]
            if new_s[i] == new_s[j]:
                j += 1
            next.append(j)
        return s[next[-1]:][::-1] + s
        
        
aacecaaa*aaacecaa
[0, 0, 1, 0, 0, 0, 1, 2, 2, 1, 2, 2, 2, 3, 4, 5, 6, 7]