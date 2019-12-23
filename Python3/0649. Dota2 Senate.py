class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        r_flag = 0
        d_flag = 0

        while 'R' in senate and 'D' in senate:
            temp = []
            for i in senate:
                if i=='R':
                    if r_flag:
                        r_flag -= 1
                    else:
                        temp.append(i)
                        d_flag += 1
                else:
                    if d_flag:
                        d_flag -= 1
                    else:
                        temp.append(i)
                        r_flag += 1
            senate = temp
        
        return 'Radiant' if 'R' in senate else "Dire"

        # R = []
        # D = []

        # l = len(senate)

        # for i in range(l):
        #     if senate[i]=='R':
        #         R.append(i)
        #     else:
        #         D.append(i)
        
        # i = 0
        # j = 0
        # lr = len(R)
        # ld = len(D)
        # while R and D:
        #     if i>=lr and j>=ld:
        #         i = 0
        #         j = 0

        #     if i>=lr:
        #         R.pop(lr-1)
        #         lr -= 1
        #         j += 1
        #     elif j>=ld:
        #         D.pop(ld-1)
        #         ld -= 1
        #         i += 1
        #     else:
        #         if R[i]>D[j]:
        #             R.pop(i)
        #             lr -= 1
        #             j += 1
        #         else:
        #             D.pop(j)
        #             ld -= 1
        #             i += 1

        # return "Radiant" if R else "Dire"
