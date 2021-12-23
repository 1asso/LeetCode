Brute force:

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        shortest = min(strs, key=len)
        for i, ch in enumerate(shortest):
            for other in strs:
                if ch != other[i]:
                    return shortest[:i]
        return shortest
        
        
Divide and conquer:

class Solution:
    def common_prefix(self, str1: str, str2: str) -> str:
        if len(str1) > len(str2):
            str1, str2 = str2, str1
        for i, ch in enumerate(str1):
            if ch != str2[i]:
                return str1[:i]
        return str1
    
    def lcp(self, strs: List[str], l: int, r: int) -> str:
        if l == r:
            return strs[l]
        mid = (l + r) // 2
        lcp_left = self.lcp(strs, l, mid)
        lcp_right = self.lcp(strs, mid + 1, r)
        return self.common_prefix(lcp_left, lcp_right)
        
    def longestCommonPrefix(self, strs: List[str]) -> str:
        return self.lcp(strs, 0, len(strs) - 1)