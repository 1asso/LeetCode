class Solution:
    def reverse(self, x: int) -> int:
        nums = []
        new_x = abs(x)
        while new_x >= 1:
            new_x, remainder = divmod(new_x, 10)
            nums.append(remainder)
        res = 0
        for num in nums:
            if res > (2 ** 31 - 1) / 10 or res < -2 ** 31 / 10:
                return 0
            res = res * 10 + num
        return -res if x < 0 else res