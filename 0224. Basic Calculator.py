class Solution:
    def calculate(self, s: str) -> int:
        operators = {
            '(': lambda a: a,
            '+': lambda a: a,
            '-': lambda a: -a
        }
        st = []
        for c in s:
            if c == ')':
                res = 0
                while True:
                    operand, operator = int(st.pop()), st.pop()
                    res += operators[operator](operand)
                    if operator == '(':
                        break
                    if st[-1] == '(':
                        st.pop()
                        break
                st.append(res)
            elif st and c.isnumeric() and st[-1].isnumeric():
                st[-1] += c
            elif c != ' ':
                st.append(c)
        res = 0
        if st[0] not in operators:
            st = ['+'] + st
        for i in range(1, len(st), 2):
            res += operators[st[i-1]](int(st[i]))
        return res