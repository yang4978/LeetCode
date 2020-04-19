class Solution:
    def getMaxRepetitions(self, s1: str, n1: int, s2: str, n2: int) -> int:
        if n1 == 0:
            return 0
        
        s1_cnt = 0
        s2_cnt = 0
        index = 0
        pos = dict()
        ans = 0
        rest = 0

        while True:
            for c in s1:
                if c == s2[index]:
                    index += 1
                    if index == len(s2):
                        s2_cnt += 1
                        index = 0
            s1_cnt += 1

            if s1_cnt == n1:
                ans = s2_cnt
                break
            
            if index in pos:
                s1_head, s2_head = pos[index]
                s1_loop = s1_cnt - s1_head
                s2_loop = s2_cnt - s2_head
                
                multi,rest = divmod(n1-s1_head,s1_loop)
                ans = multi*s2_loop + s2_head

                break
            
            else:
                pos[index] = (s1_cnt,s2_cnt)
        
        while rest:
            for c in s1:
                if c == s2[index]:
                    index += 1
                    if index == len(s2):
                        ans += 1
                        index = 0
            rest -= 1
        
        return ans//n2
