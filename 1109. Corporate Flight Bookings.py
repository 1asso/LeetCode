Similar to Q370:

class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        answer = [0] * n
        for first, last, seats in bookings:
            first -= 1
            last -= 1
            answer[first] += seats
            if last + 1 < n:
                answer[last + 1] -= seats
        for i in range(1, n):
            answer[i] += answer[i - 1]
        return answer