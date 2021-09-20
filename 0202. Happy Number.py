class Solution:
    def isHappy(self, n: int) -> bool:
        hashset = set()        
        while n != 1:
            res = 0
            while n > 0:
                n, m = n // 10, n % 10
                res += m * m
            n = res
            if n in hashset:
                return False
            hashset.add(n)
        return True