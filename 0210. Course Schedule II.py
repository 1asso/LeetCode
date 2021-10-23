Topological sort:

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # init
        neighbors = defaultdict(list)
        in_degree = {}
        path = []
        for dest, src in prerequisites:
            neighbors[src].append(dest)
            in_degree[dest] = in_degree.get(dest, 0) + 1
        zero_indegree_queue = deque([i for i in range(numCourses) if i not in in_degree])
        
        # loop the graph
        while zero_indegree_queue:
            vertex = zero_indegree_queue.popleft()
            path.append(vertex)
            for neighbor in neighbors[vertex]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    zero_indegree_queue.append(neighbor)
                    
        return path if len(path) == numCourses else []
      
      
DFS:
  
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
