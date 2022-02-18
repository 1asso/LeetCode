class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        graph = defaultdict(set)
        for i, route in enumerate(routes):
            for j in route:
                graph[j].add(i)
        visited = set([source])
        queue = deque([(source, 0)])
        while queue:
            for i in range(len(queue)):
                stop, depth = queue.popleft()
                if stop == target:
                    return depth
                for i in graph[stop]:
                    for node in routes[i]:
                        if node not in visited:
                            visited.add(node)
                            queue.append((node, depth + 1))
                    routes[i] = []
        return -1