#You are given an array of transactions transactions where transactions[i] = [fromi, toi, amounti] indicates that the person with ID = fromi gave amounti $ to the person with ID = toi.

#Return the minimum number of transactions required to settle the debt.

 

#Example 1:

#Input: transactions = [[0,1,10],[2,0,5]]
#Output: 2
#Explanation:
#Person #0 gave person #1 $10.
#Person #2 gave person #0 $5.
#Two transactions are needed. One way to settle the debt is person #1 pays person #0 and #2 $5 each.

#Example 2:

#Input: transactions = [[0,1,10],[1,0,1],[1,2,5],[2,0,5]]
#Output: 1
#Explanation:
#Person #0 gave person #1 $10.
#Person #1 gave person #0 $1.
#Person #1 gave person #2 $5.
#Person #2 gave person #0 $5.
#Therefore, person #1 only need to give person #0 $4, and all debt is settled.

class Solution:
    def minTransfers(self, transactions: List[List[int]]) -> int:
        m = defaultdict(int)
        for t in transactions:
            m[t[0]] -= t[2]
            m[t[1]] += t[2]
        debt = list(m.values())
        
        def backtracking(p):
            while (p < len(debt) and not debt[p]):
                p += 1
            if p == len(debt):
                return 0
            res = float('inf')
            for i in range(p + 1, len(debt)):
                if debt[p] * debt[i] < 0:
                    debt[i] += debt[p]
                    res = min(res, 1 + backtracking(p + 1))
                    debt[i] -= debt[p]
            return res
        
        return backtracking(0)