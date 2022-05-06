# find previous less, next less
class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        st = []
        l, r = [-1] * len(arr), [len(arr)] * len(arr)
        for i in range(len(arr)):
            while st and arr[i] < arr[st[-1]]:
                r[st.pop()] = i
            if st: l[i] = st[-1]
            st.append(i)
        return sum(arr[i] * (i - l[i]) * (r[i] - i) for i in range(len(arr))) % (10 ** 9 + 7)