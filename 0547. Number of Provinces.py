This is different from Number of Islands:

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        length = len(isConnected)
        visited = set()
        def dfs(node):
            if node in visited:
                return
            visited.add(node)
            for nei, adj in enumerate(isConnected[node]):
                if adj and nei not in visited:
                    dfs(nei)
        res = 0
        for i in range(length):
            if i not in visited:
                res += 1
                dfs(i)
        return res