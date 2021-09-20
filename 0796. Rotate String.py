Brute-force O(N^2):

class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        return len(goal) == len(s) and goal in s+s


KMP O(N):

class Solution:
    def compute(self, goal) -> list[int]:
        next = [0, 0]
        j = 0
        for i in range(1, len(goal)):
            while j > 0 and goal[i] != goal[j]:
                j = next[j]
            if goal[i] == goal[j]:
                j += 1
            next.append(j)
        return next
            
    def rotateString(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False
        if len(s) == 0:
            return True
        s = s + s
        res = []
        j = 0
        
        next = self.compute(goal)
        
        for i in range(0, len(s)):
            while j > 0 and s[i] != goal[j]:
                j = next[j]
            if s[i] == goal[j]:
                j += 1
            if j == len(goal):
                return True
            
        return False