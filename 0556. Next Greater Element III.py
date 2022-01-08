class Solution:
    def nextGreaterElement(self, n: int) -> int:
        digits = list(str(n))
        index = -1
        for i in reversed(range(len(digits) - 1)):
            if digits[i] < digits[i + 1]:
                index = i
                break
        if index < 0:
            return index
        else:
            digits[index+1:] = digits[index+1:][::-1]
            greater = bisect.bisect_right(digits, digits[index], index + 1, len(digits))
            digits[index], digits[greater] = digits[greater], digits[index]
            res = int(''.join(digits))
            return res if res < 1 << 31 else -1