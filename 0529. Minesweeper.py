class Solution:
    def check(self, board, clicks):
        count = 0
        for x, y in clicks:
                if 0 <= x < len(board) and 0 <= y < len(board[0])\
                and board[x][y] in ['M', 'X']:
                    count += 1
        return count
    
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        val = board[click[0]][click[1]]
        if val == 'E':
            clicks = [[click[0] + x, click[1] + y] \
                      for x in [-1, 0, 1] for y in [-1, 0, 1] if x or y]
            count = self.check(board, clicks)
            if count:
                board[click[0]][click[1]] = str(count)
            else:
                board[click[0]][click[1]] = 'B'
                for x, y in clicks:
                    if 0 <= x < len(board) and 0 <= y < len(board[0]):
                        self.updateBoard(board, [x, y])
        elif val == 'M':
            board[click[0]][click[1]] = 'X'
        return board