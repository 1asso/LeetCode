class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        res = list(s)
        for i in range(0, len(s), 2 * k):
            l, r = i, min(i+k, len(s))-1
            while l <= r:
                res[l], res[r] = res[r], res[l]
                l += 1
                r -= 1
        return "".join(res)
        
 OR:
 
 class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        res = list(s)
        for i in range(0, len(s), 2 * k):
            res[i:i+k] = reversed(res[i:i+k])
        return "".join(res)