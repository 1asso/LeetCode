Prefix Sums:

class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        p = [0]
        for c in s:
            p.append(p[-1] + int(c))
        return min(p[i] + len(s) - i - (p[-1] - p[i]) for i in range(len(p)))

# For example, with S = "010110": we have P = [0, 0, 1, 1, 2, 3, 3]. 

# Now say we want to evaluate having x=3 zeros.

# There are P[3] = 1 ones in the first 3 characters, and P[6] - P[3] = 2 ones in the later N-x = 3 characters.

# So, there is (N-x) - (P[N] - P[x]) = 1 zero in the later N-x characters.

# We take the minimum among all candidate answers to arrive at the final answer.