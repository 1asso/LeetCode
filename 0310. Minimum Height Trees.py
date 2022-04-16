Topological sort:

class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        neighbors = collections.defaultdict(set)
        for start, end in edges:
            neighbors[start].add(end)
            neighbors[end].add(start)
        leaves = collections.deque([i for i in range(n) if len(neighbors[i]) <= 1])
        remaining_nodes = n
        while leaves:
            if remaining_nodes <= 2:
                return leaves
            remaining_nodes -= len(leaves)
            for _ in range(len(leaves)):
                leaf = leaves.popleft()
                neighbor = neighbors[leaf].pop()
                neighbors[neighbor].remove(leaf)
                if len(neighbors[neighbor]) == 1:
                    leaves.append(neighbor)