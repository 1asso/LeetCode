Backtracking:

class Solution:    
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def backtracking(s, l, r):
            if len(s) == 2 * n:
                res.append(s)
            if l < n:
                backtracking(s+'(', l+1, r)
            if r < l:
                backtracking(s+')', l, r+1)
        backtracking('', 0, 0)
        return res