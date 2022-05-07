Similar to Q370:

class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        length = max(list(zip(*trips))[2]) + 1
        res = [0] * (length + 1)
        for val, start, end in trips:
            res[start] += val
            res[end] -= val
        for i in range(length):
            res[i] += res[i - 1]
            if res[i] > capacity:
                return False
        return True