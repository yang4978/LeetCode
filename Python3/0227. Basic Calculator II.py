class Solution:
    def calculate(self, s: str) -> int:
        presign = '+'
        s = s+'+'
        ss = []
        temp = 0
        for c in s:
            if c == ' ':
                continue
            elif c.isdigit():
                temp = temp*10+int(c)
            else:
                if presign == '+':
                    ss.append(temp)
                elif presign == '-':
                    ss.append(-temp)
                elif presign == '*':
                    ss[-1] *= temp
                else:
                    ss[-1] = int(ss[-1]/temp)
                temp = 0
                presign = c
        return sum(ss)
