BFS:

class Solution:
    def next_states(self, cur_state):
        next_states = []
        for i, ch in enumerate(cur_state):
            n = int(ch)
            next_states.append(cur_state[:i] + str((n + 1) % 10) + cur_state[i + 1:])
            next_states.append(cur_state[:i] + str((n - 1) % 10) + cur_state[i + 1:])
        return next_states
    
    def openLock(self, deadends: List[str], target: str) -> int:
        queue = deque(['0000'])
        visited = set(deadends)
        moves = 0
        while queue:
            for _ in range(len(queue)):
                cur = queue.popleft()
                if cur == target:
                    return moves
                if cur not in visited:
                    visited.add(cur)
                    queue.extend(self.next_states(cur))
            moves += 1
        return -1