# Given an array of meeting time intervals intervals where intervals[i] = [starti, endi], return the minimum number of conference rooms required.

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
      
      
Priority Queue:
  
import queue
class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[0])
        q = queue.PriorityQueue()
        q.put(intervals[0][1])
        for i in range(1, len(intervals)):
            top = q.get()
            if intervals[i][0] < top:
                q.put(top)
            q.put(intervals[i][1])
        return q.qsize()
