Two pointers:

class Solution:
    def reorganizeString(self, s: str) -> str:
        s = sorted(sorted(s), key=s.count, reverse=True)
        mid = ceil(len(s) / 2)
        if s[0] == s[mid]:
            return ''
        s[::2], s[1::2] = s[:mid], s[mid:]
        return ''.join(s)