class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        visited = set()
        
        def dfs(node):
            if node in visited:
                return 0
            visited.add(node)
            secs = 0
            for child in graph[node]:
                secs += dfs(child)
            if secs:
                return secs + 2
            return 2 if hasApple[node] else 0
        
        return max(dfs(0) - 2, 0)1448. Count Good Nodes in Binary Tree