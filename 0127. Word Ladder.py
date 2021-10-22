class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        adjacency = defaultdict(set)
        for word in wordList:
            for i in range(len(word)):
                adjacency[word[:i]+'*'+word[i+1:]].add(word)
        #bfs
        q = deque([beginWord])
        visited = set([beginWord])
        res = 1
        while q:
            for _ in range(len(q)):
                cur = q.popleft()
                if cur == endWord:
                    return res
                visited.add(cur)
                for i in range(len(cur)):
                    pattern = cur[:i] + '*' + cur[i+1:]
                    for word in adjacency[pattern]:
                        if word not in visited:
                            q.append(word)
                            visited.add(word)
            res += 1
        return 0
