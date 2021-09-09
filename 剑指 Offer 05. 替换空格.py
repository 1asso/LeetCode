class Solution:
    def replaceSpace(self, s: str) -> str:
        dict_s = Counter(s)
        len_space = dict_s[' ']
        res = [None] * (len(s) + 2 * len_space)
        l, r = len(s)-1, len(res)-1
        while l >= 0:
            if s[l] == ' ':
                res[r-2:r+1] = "%20"
                r -= 3
            else:
                res[r] = s[l]
                r -= 1
            l -= 1
        return "".join(res)