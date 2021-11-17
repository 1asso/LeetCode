class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m, n = len(board), len(board[0])
        def backtracking(row, col, word):
            if not word:
                return True
            letter = board[row][col]
            board[row][col] = None
            for r_offset, c_offset in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                new_row, new_col = row + r_offset, col + c_offset
                if 0 <= new_row < m and 0 <= new_col < n and \
                    board[new_row][new_col] == word[0]:
                    if backtracking(new_row, new_col, word[1:]):
                        return True
            board[row][col] = letter
            return False
        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0]:
                    if backtracking(i, j, word[1:]):
                        return True
        return False
