BFS:

class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        d = defaultdict(list)
        for i in range(len(values)):
            d[equations[i][0]].append([equations[i][1], values[i]])
            d[equations[i][1]].append([equations[i][0], 1 / values[i]])
        
        def bfs(q):
            src, target = q
            if src not in d or target not in d:
                return -1
            queue = deque([[src, 1]])
            visited = {src}
            while queue:
                cur, val = queue.popleft()
                if cur == target:
                    return val
                for k, v in d[cur]:
                    if k not in visited:
                        visited.add(k)
                        queue.append([k, v * val])
            return -1
        
        res = []
        for q in queries:
            res.append(bfs(q))

        return res