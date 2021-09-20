class Solution:
    def check(self, board, cand, x, y):
        if cand in board[x] or cand in [r[y] for r in board]:
            return False
        for r in board[x//3*3:(x//3+1)*3]:
            if cand in r[y//3*3:(y//3+1)*3]:
                return False
        return True
        
    def backtracking(self, board, x, y):
        while board[x][y] != '.':
            y += 1
            if y == 9: y, x = 0, x+1
            if x == 9: return True
            
        for i in range(1, 10):
            if self.check(board, str(i), x, y):
                board[x][y] = str(i)
                if self.backtracking(board, x, y):
                    return True
        board[x][y] = '.'
        return False
        
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        assert(self.backtracking(board, 0, 0))
        
        
OR:

class Solution:
    def check(self, board, cand, x, y):
        if cand in board[x] or cand in [r[y] for r in board]:
            return False
        for r in board[x//3*3:(x//3+1)*3]:
            if cand in r[y//3*3:(y//3+1)*3]:
                return False
        return True
        
    def backtracking(self, board, index):
        if index == 81: return True
        x, y = index // 9, index % 9
            
        if board[x][y] == '.':
            for i in range(1, 10):
                if self.check(board, str(i), x, y):
                    board[x][y] = str(i)
                    if self.backtracking(board, index+1):
                        return True
            board[x][y] = '.'
        else:
            if self.backtracking(board, index+1):
                    return True
        return False
        
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        assert(self.backtracking(board, 0))