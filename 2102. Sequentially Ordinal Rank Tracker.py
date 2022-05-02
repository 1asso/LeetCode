import heapq

class Node:
    
    def __init__(self, score, name):
        self.score = score
        self.name = name
    
    def __lt__(self, obj):
        return self.name > obj.name if self.score == obj.score else self.score < obj.score

class SORTracker:

    def __init__(self):
        self.max = []
        self.min = []
        self.count = 0

    def add(self, name: str, score: int) -> None:
        heapq.heappush(self.min, (Node(score, name)))
        while len(self.min) > self.count:
            node = heapq.heappop(self.min)
            heapq.heappush(self.max, (-node.score, node.name))

    def get(self) -> str:
        self.count += 1
        score, name = heapq.heappop(self.max)
        heapq.heappush(self.min, Node(-score, name))
        return name


# Your SORTracker object will be instantiated and called as such:
# obj = SORTracker()
# obj.add(name,score)
# param_2 = obj.get()