class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        start = res = 0
        tracker = {}
        for end in range(len(fruits)):
            c = fruits[end]
            tracker[c] = tracker.get(c, 0) + 1
            while len(tracker) > 2:
                    c = fruits[start]
                    tracker[c] -= 1
                    if tracker[c] == 0:
                        del tracker[c]
                    start += 1
            res = max(res, end - start + 1)
        return res