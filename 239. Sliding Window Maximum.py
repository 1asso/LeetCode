class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        q = deque()
        for i in range(len(nums)):
            while q and nums[i] > q[-1]:
                q.pop()
            q.append(nums[i])
            if i >= k and nums[i-k] == q[0]:
                q.popleft()
            res.append(q[0])
                
        return res[k-1:]