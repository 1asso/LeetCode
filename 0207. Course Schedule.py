class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)
        indegree = {}
        for dest, src in prerequisites:
            graph[src].append(dest)
            indegree[dest] = indegree.get(dest, 0) + 1
        zero_indegree = [node for node in range(numCourses) if node not in indegree]
        while zero_indegree:
            vertex = zero_indegree.pop()
            for node in graph[vertex]:
                indegree[node] -= 1
                if indegree[node] == 0:
                    zero_indegree.append(node)
                    indegree.pop(node)
        return not len(indegree)