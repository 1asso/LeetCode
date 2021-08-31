class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def compute(s):
            s = list(s)
            last = 0
            for i in range(0, len(s)):
                if s[i] == '#':
                    last = last - 1 if last > 0 else 0
                else:
                    s[last] = s[i]
                    last += 1
            return s[:last]
        return compute(s) == compute(t)