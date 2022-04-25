BFS:

class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        children = defaultdict(list)
        for i in range(n):
            children[manager[i]].append(i)
        queue = deque([(headID, informTime[headID])])
        res = 0
        while queue:
            node, time = queue.popleft()
            if node not in children:
                res = max(time, res)
            for child in children[node]:
                queue.append((child, informTime[child] + time))
        return res
        
        
DFS:

class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        children = defaultdict(list)
        for i in range(n):
            children[manager[i]].append(i)
        def dfs(node):
            res = 0
            for child in children[node]:
                res = max(res, informTime[node] + dfs(child))
            return res
        return dfs(headID)