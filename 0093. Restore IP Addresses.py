class Solution:
    def backtracking(self, s, path, res, index):
        if len(path) == 4 and index == len(s):
            res.append('.'.join(path))
        else:
            for i in range(index, len(s)):
                if len(s) - index > 3 * (4 - len(path)):
                    return
                p = s[index:i+1]
                if int(p) > 255 or (s[index] == '0' and i > index):
                    return
                path.append(p)
                self.backtracking(s, path, res, i+1)
                path.pop()
                
    def restoreIpAddresses(self, s: str) -> List[str]:
        res = []
        self.backtracking(s, [], res, 0)
        return res