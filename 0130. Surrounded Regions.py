class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m, n = len(board), len(board[0])
        connected_to_boundary = set()
        queue = deque([])

        for x in range(m):
            for y in range(n):
                if (x in [0, m - 1] or y in [0, n - 1]) and board[x][y] == 'O':
                    queue.append((x, y))
                    
        while queue:
            x, y = cur = queue.popleft()
            if cur not in connected_to_boundary:
                connected_to_boundary.add(cur)
                for new_x, new_y in [[x + 1, y], [x - 1, y], [x, y + 1], [x, y - 1]]:
                    if 0 <= new_x < m and 0 <= new_y < n and board[new_x][new_y] == 'O':
                        queue.append((new_x, new_y))
        
        for i in range(1, m):
            for j in range(1, n):
                if (i, j) not in connected_to_boundary:
                    board[i][j] = 'X'