# 0: "dead" 2: "dead->live"
# 1: "live" 3: "live->dead"

class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m, n = len(board), len(board[0])
        def check_neighbors(i, j):
            count = 0
            for i_offset, j_offset in [(x, y) for x in [-1, 0, 1] for y in [-1, 0, 1]]:
                new_i, new_j = i + i_offset, j + j_offset
                if (i_offset or j_offset) and \
                    0 <= new_i < m and 0 <= new_j < n and \
                    board[new_i][new_j] % 2 == 1:
                    count += 1
            return count
        
        for i in range(m):
            for j in range(n):
                if board[i][j] == 0 and check_neighbors(i, j) == 3:
                    board[i][j] = 2
                if board[i][j] == 1 and not 2 <= check_neighbors(i, j) <= 3:
                    board[i][j] = 3
        for i in range(m):
            for j in range(n):
                board[i][j] = 3 - board[i][j] if board[i][j] > 1 else board[i][j]