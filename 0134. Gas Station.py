class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        start, cur_sum, total_sum = 0, 0, 0
        for i in range(len(gas)):
            cur_sum += gas[i] - cost[i]
            total_sum += gas[i] - cost[i]
            if cur_sum < 0:
                start, cur_sum = i + 1, 0
        return start if total_sum >= 0 else -1