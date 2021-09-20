class Solution:
    def generateMatrix(self, n):
        matrix, lo = [[n*n]], n*n
        while lo > 1:
            lo, hi = lo - len(matrix), lo
            matrix = [range(lo, hi)] + list(zip(*matrix[::-1]))
        return matrix