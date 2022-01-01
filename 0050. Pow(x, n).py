class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n < 0:
            return 1 / x * self.myPow(1 / x, abs(n) - 1)
        if n == 0:
            return 1
        half = self.myPow(x, n // 2)
        if n % 2:
            return x * half * half
        else:
            return half * half