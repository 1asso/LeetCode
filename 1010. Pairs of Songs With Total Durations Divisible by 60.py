class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        hashtb = {}
        res = 0
        for t in time:
            cur, pair = t % 60, (60 - t % 60) % 60
            res += hashtb.get(pair, 0)
            hashtb[cur] = hashtb.get(cur, 0) + 1
        return res
