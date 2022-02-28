class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        counter = Counter()
        i = 0
        for j in range(len(fruits)):
            counter[fruits[j]] += 1
            if len(counter) > 2:
                counter[fruits[i]] -= 1
                if counter[fruits[i]] == 0:
                    counter.pop(fruits[i])
                i += 1
        return j - i + 1