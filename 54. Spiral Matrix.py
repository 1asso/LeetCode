class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []
        while len(matrix):
            res += matrix.pop(0)
            matrix = list(zip(*matrix))[::-1]
            
        return res
        


In recursion:

class Solution:
    def spiralOrder(self, matrix):
        return matrix and [*matrix.pop(0)] + self.spiralOrder([*zip(*matrix)][::-1])