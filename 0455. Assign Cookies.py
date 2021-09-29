class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        s.sort()
        g.sort()
        res = 0
        for i in range(len(s)):
            if g[res] <= s[i]:
                res += 1
            if res == len(g): break
        return res