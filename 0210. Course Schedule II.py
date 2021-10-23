Topological sort:
  
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        self.white = 1
        self.grey = 2
        self.black = 3
        
        adj_list = defaultdict(list)
        for dest, src in prerequisites:
            adj_list[src].append(dest)
        path = []
        self.is_possible = True
        colors = {i: self.white for i in range(numCourses)}
        
        def dfs(node):
            if not self.is_possible:
                return
            colors[node] = self.grey
            for neighbor in adj_list[node]:
                if colors[neighbor] == self.grey:
                    self.is_possible = False
                    return
                elif colors[neighbor] == self.white:
                    dfs(neighbor)
                
            colors[node] = self.black
            path.append(node)
        
        for vertex in range(numCourses):
            if colors[vertex] == self.white:
                dfs(vertex)
        return path[::-1] if self.is_possible else []
