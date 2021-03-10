class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        res = 0
        for c in s:
            if c == ' ':
                continue

            elif c == ')':
                i = stack.pop()
                power = 1
                res = 0
                temp = 0
                while i != '(':
                    if i == '+':
                        res += temp
                        temp = 0
                        power = 1
                    elif i == '-':
                        res -= temp
                        temp = 0
                        power = 1
                    else:
                        temp += power*int(i)
                        power *= 10

                    i = stack.pop()
                
                res += temp

                stack.append(str(res))

            else:
                stack.append(c)
        
        power = 1
        res = 0
        temp = 0

        while stack!=[]:
            i = stack.pop()
            if i == '+' or i == '(':
                res += temp
                temp = 0
                power = 1
            elif i == '-':
                res -= temp
                temp = 0
                power = 1
            else:
                temp += power*int(i)
                power *= 10
        res += temp

        return res
