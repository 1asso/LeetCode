class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        mono_st = []
        for i in range(len(temperatures)):
            while mono_st and temperatures[mono_st[-1]] < temperatures[i]:
                index = mono_st.pop()
                res[index] = i - index
            mono_st.append(i)
        return res