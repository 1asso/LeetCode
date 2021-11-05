class Solution:    
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        # construct trie
        word_key = '$'
        trie = {}
        for word in words:
            cur = trie
            for letter in word:
                cur = cur.setdefault(letter, {})
            cur[word_key] = word
            
        # backtracking
        res = []
        m, n = len(board), len(board[0])
        
        def backtracking(trie, row, col):
            letter = board[row][col]
            cur = trie[letter]
            if word_key in cur:
                res.append(cur.pop(word_key))
            if not cur:
                trie.pop(letter)
            board[row][col] = '#'
            for r_offset, c_offset in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                r_new, c_new = row + r_offset, col + c_offset
                if 0 <= r_new < m and 0 <= c_new < n and \
                    board[r_new][c_new] in cur:
                    backtracking(cur, r_new, c_new)
            board[row][col] = letter
        
        for i in range(m):
            for j in range(n):
                if board[i][j] in trie:
                    backtracking(trie, i, j)
        return res
