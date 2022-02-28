# Sliding window with monotonic queue (deque)

class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        mind = collections.deque() # [1, 2, 3, 4]
        maxd = collections.deque() # [4, 3, 2, 1]
        start = 0
        for num in nums:
            while mind and num < mind[-1]:
                mind.pop()
            while maxd and num > maxd[-1]:
                maxd.pop()
            mind.append(num)
            maxd.append(num)
            if maxd[0] - mind[0] > limit:
                # Why do we check only maxd[0]/mind[0] to remove A[i]?
                # Take maxd as an example. In order for A[i] to be present in maxd, 
                # A[i] >= A[x], where x = i+1...j. 
                # In other words, it has to be the biggest element or 
                # it would have already been removed. 
                # The biggest element would be in maxd[0]. 
                # Similar explanation applies for mind.
                if nums[start] == mind[0]:
                    mind.popleft()
                if nums[start] == maxd[0]:
                    maxd.popleft()
                start += 1
        return len(nums) - start 