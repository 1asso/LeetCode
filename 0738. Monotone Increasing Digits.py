class Solution:
    def monotoneIncreasingDigits(self, n: int) -> int:
        l = list(str(n))
        for i in reversed(range(1, len(l))):
            if int(l[i-1]) > int(l[i]):
                l[i:] = '9' * len(l[i:])
                l[i-1] = str(int(l[i-1])-1)
        return int(''.join(l))