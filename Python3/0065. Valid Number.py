class Solution:
    def isNumber(self, s: str) -> bool:
        flag_dot = 0
        flag_e = 0
        flag_pn = 0
        flag_num = 0

        s = s.strip()

        for c in s:
            if c.isdigit():
                flag_num = 1
            elif c == '.':
                if flag_dot == 0 and flag_e == 0:
                    flag_dot = 1
                else:
                    return False
            elif c == 'e' or c == 'E':
                if flag_num == 1 and flag_e == 0:
                    flag_e = 1
                    flag_num = 0
                else:
                    return False
            elif c == '+' or c == '-':
                if ((flag_pn == 0 and flag_dot == 0)or flag_e == 1) and flag_num == 0:
                    flag_pn = 1
                else:
                    return False
            else:
                return False
        
        return flag_num == 1
