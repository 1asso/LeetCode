class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        total_sum, cur_sum, start = 0, 0, 0
        for i in range(len(gas)):
            cur_sum += gas[i] - cost[i]
            total_sum += gas[i] - cost[i]
            if cur_sum < 0:
                cur_sum, start = 0, i+1
        if total_sum < 0: return -1
        return start