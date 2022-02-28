class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        counter = {c: 0 for c in 'abc'}
        l, res = 0, 0
        for r in range(len(s)):
            counter[s[r]] += 1
            while all(counter.values()):
                res += len(s) - r
                counter[s[l]] -= 1
                l += 1
        return res