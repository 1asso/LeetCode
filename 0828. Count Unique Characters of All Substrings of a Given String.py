# Ref: https://leetcode.com/problems/count-unique-characters-of-all-substrings-of-a-given-string/discuss/128952/C%2B%2BJavaPython-One-pass-O(N)
# XXAXXXAXA
# 012345678
class Solution:
    def uniqueLetterString(self, s: str) -> int:
        index = {c:[-1, -1] for c in string.ascii_uppercase}
        res = 0
        for i, c in enumerate(s):
            j, k = index[c]
            res += (i - k) * (k - j)
            index[c] = [k, i]
        for c in index:
            j, k, i = *index[c], len(s)
            res += (i - k) * (k - j)
        return res
