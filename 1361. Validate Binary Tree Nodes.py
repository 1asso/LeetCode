DFS:

class Solution:
    def validateBinaryTreeNodes(self, n: int, leftChild: List[int], rightChild: List[int]) -> bool:
        root = (set(range(n)) - set(leftChild + rightChild))
        if len(root) != 1:
            return False
        visited = set()
        def dfs(node):
            if node == -1:
                return True
            if node in visited:
                return False
            visited.add(node)
            l = dfs(leftChild[node])
            r = dfs(rightChild[node])
            return l and r
            
        res = dfs(root.pop())
        return res and len(visited) == n
        
        
        
BFS:

class Solution:
    def validateBinaryTreeNodes(self, n: int, leftChild: List[int], rightChild: List[int]) -> bool:
        root = (set(range(n)) - set(leftChild + rightChild))
        if len(root) != 1:
            return False
        visited = set()
        
        queue = deque([root.pop()])
        while queue:
            for _ in range(len(queue)):
                node = queue.popleft()
                if node in visited:
                    return False
                visited.add(node)
                queue.extend([child for child in [leftChild[node], rightChild[node]] if child != -1])
        
        return len(visited) == n