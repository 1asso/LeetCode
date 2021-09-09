Brute-force O(M+N):

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle in haystack:
            n = len(needle)
            for i in range(len(haystack)-n+1):
                if needle == haystack[i:i+n]:
                    return i
        else:
            return -1
            

KMP O(N):

class Solution:
    def compute(self, needle):
        next = [0, 0]
        j = 0
        for i in range(1, len(needle)):
            if j > 0 and needle[i] != needle[j]:
                j = next[j]
            if needle[i] == needle[j]:
                j += 1
            next.append(j)
        return next
    
    def strStr(self, haystack: str, needle: str) -> int:
        if needle == "": return 0
        next = self.compute(needle)
        res = []
        j = 0
        
        for i in range(len(haystack)):
            while j > 0 and haystack[i] != needle[j]:
                j = next[j]
            if haystack[i] == needle[j]:
                j += 1
            if j == len(needle):
                return i-j+1 
        return -1