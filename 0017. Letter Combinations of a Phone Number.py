class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        letters = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', 
            '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}
        res = []
        def backtracking(index, combination):
            if len(combination) == len(digits):
                if combination:
                    res.append(combination)
                return
            for c in letters[digits[index]]:
                backtracking(index + 1, combination + c)
        backtracking(0, '')
        return res