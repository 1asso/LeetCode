# Given an array of meeting time intervals where intervals[i] = [starti, endi], return the minimum number of conference rooms required.

# Example 1:
# Input: intervals = [[0,30],[5,10],[15,20]]
# Output: 2

# Example 2:
# Input: intervals = [[7,10],[2,4]]
# Output: 1


Greedy:

class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        starts = sorted(i[0] for i in intervals)
        ends = sorted(i[1] for i in intervals)
        e = 0
        available = numRooms = 0
        for s in starts:
            while s >= ends[e]:
                e += 1
                available += 1
            if available:
                available -= 1
            else:
                numRooms += 1
        return numRooms
      
      
Heap:

class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        heap = []
        intervals.sort(key=lambda x: x[0])
        heapq.heappush(heap, intervals[0][1])
        for start, end in intervals[1:]:
            if start >= heap[0]:
                heapq.heappop(heap)
            heapq.heappush(heap, end)
        return len(heap)
