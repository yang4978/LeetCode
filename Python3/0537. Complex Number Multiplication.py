class Solution:
    def complexNumberMultiply(self, a: str, b: str) -> str:
        def complexNumber(s):
            res = [1,1]
            if s[0]=='-':
                res[0] = -1
                s = s[1:]
            temp = 0
            
            for i in s:
                if i == '+':
                    res[0] *= temp
                    temp = 0
                elif i == '-':
                    res[1] = -1 if i=='-' else 1
                elif i=='i':
                    res[1] *= temp
                else:
                    temp = temp*10 + int(i)
            return res
            
        com_a = complexNumber(a)
        com_b = complexNumber(b)
        return str(com_a[0]*com_b[0]-com_a[1]*com_b[1])+'+'+str(com_a[0]*com_b[1]+com_a[1]*com_b[0])+'i'
