class Solution:
    def getFood(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])
        def next_move(x, y):
            for nx, ny in [[x, y + 1], [x, y - 1], [x + 1, y], [x - 1, y]]:
                if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] in ['O', '#']:
                    yield nx, ny
        queue = deque([])
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '*':
                    queue.append((i, j))
                    break
            if queue:
                break
        move = 0
        while queue:            
            move += 1
            for _ in range(len(queue)):
                for nx, ny in next_move(*queue.popleft()):
                    if grid[nx][ny] == '#':
                        return move
                    grid[nx][ny] = '+'
                    queue.append((nx, ny))
        return -1
        
        
        
You are starving and you want to eat food as quickly as possible. You want to find the shortest path to arrive at any food cell.

You are given an m x n character matrix, grid, of these different types of cells:

'*' is your location. There is exactly one '*' cell.
'#' is a food cell. There may be multiple food cells.
'O' is free space, and you can travel through these cells.
'X' is an obstacle, and you cannot travel through these cells.
You can travel to any adjacent cell north, east, south, or west of your current location if there is not an obstacle.

Return the length of the shortest path for you to reach any food cell. If there is no path for you to reach food, return -1.