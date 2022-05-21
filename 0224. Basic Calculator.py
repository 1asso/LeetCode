class Solution:
    def calculate(self, s: str) -> int:
        num, st, op = 0, [], '+'
        s += '+'
        ops = {
            '+': lambda num: st.append(num),
            '-': lambda num: st.append(-num)
        }
        for c in s:
            if c.isnumeric():
                num = num * 10 + int(c)
            elif c in ops:
                ops[op](num)
                num, op = 0, c
            elif c == '(':
                st.append(op)
                op = '+'
            elif c == ')':
                ops[op](num)
                num, op = 0, c
                while st[-1] not in ops:
                    num += st.pop()
                ops[st.pop()](num)
                num, op = 0, '+'
        return sum(st)