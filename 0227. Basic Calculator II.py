class Solution:
    def calculate(self, s: str) -> int:
        num, st, op = 0, [], '+'
        s += '+'
        ops = {
            '+': lambda num: st.append(num),
            '-': lambda num: st.append(-num),
            '*': lambda num: st.append(st.pop() * num),
            '/': lambda num: st.append(int(st.pop() / num))
        }
        for c in s:
            if c.isnumeric():
                num = num * 10 + int(c)
            elif c != ' ':
                ops[op](num)
                op, num = c, 0
        return sum(st)