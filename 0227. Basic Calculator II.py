class Solution:
    def calculate(self, s: str) -> int:
        s = re.split('(\D)', s.replace(' ', ''))
        operators = {
            '+': lambda a: a,
            '-': lambda a: -a,
            '*': lambda a, b: a * b,
            '/': lambda a, b: a // b
        }
        st = ['+']
        for c in s:
            if st[-1] in ['*', '/']:
                st.append(operators[st.pop()](int(st.pop()), int(c)))
            else:
                st.append(c)
        res = 0
        for i in range(1, len(st), 2):
            res += operators[st[i-1]](int(st[i]))
        return res