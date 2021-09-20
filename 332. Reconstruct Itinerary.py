class Solution:
    def backtracking(self, tickets, path, t_dict):
        if len(path) == len(tickets) + 1:
            return True
        start = path[-1]
        t_dict[start].sort()
        for _ in t_dict[start]:
            t = t_dict[start].pop(0)
            path.append(t)
            if self.backtracking(tickets, path, t_dict):
                return True
            path.pop()
            t_dict[start].append(t)

    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        path = ['JFK']
        t_dict = defaultdict(list)
        for t in tickets:
            t_dict[t[0]].append(t[1])
        self.backtracking(tickets, path, t_dict)
        return path