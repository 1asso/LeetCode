class Item:
    def __init__(self, freq, word):
        self.freq = freq
        self.word = word
    
    def __lt__(self, other):
        if self.freq == other.freq:
            return self.word < other.word
        else:
            return self.freq > other.freq

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        counter = collections.Counter(words)
        heap = []
        for word, freq in counter.items():
            heapq.heappush(heap, Item(freq, word))
        res = []
        for _ in range(k):
            res.append(heapq.heappop(heap).word)
        return res
        
        
OR:

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        counter = collections.Counter(words)
        res = heapq.nsmallest(k, counter, key=lambda word: [-counter[word], word])
        return res