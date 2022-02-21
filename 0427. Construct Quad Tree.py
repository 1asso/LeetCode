"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution:    
    def construct(self, grid: List[List[int]]) -> 'Node':
        if not grid:
            return None
        if self.is_leaf(grid):
            return Node(grid[0][0], True, None, None, None, None)
        n = len(grid)
        return Node(0, False,
                   self.construct([row[0:n // 2] for row in grid[0:n // 2]]),
                   self.construct([row[n // 2:n] for row in grid[0:n // 2]]),
                   self.construct([row[0:n // 2] for row in grid[n // 2:n]]),
                   self.construct([row[n // 2:n] for row in grid[n // 2:n]]))
    
    def is_leaf(self, grid):
        return all(grid[i][j] == grid[0][0] \
                   for i in range(len(grid)) for j in range(len(grid)))