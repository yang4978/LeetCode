class Solution:
    def minWindow(self, s: str, t: str) -> str:
        lt = len(t)
        ls = len(s)
        #letter = collections.Counter(t)
        letter = {}

        for i in t:
            if i not in letter:
                letter[i] = 1
            else:
                letter[i] += 1
        
        l = 0
        r = 0

        res = ["",ls+1]

        while r<ls:
            c = s[r]
            if lt:
                r += 1
                if c in letter:
                    letter[c] -= 1
                    if letter[c]>=0:
                        lt -= 1

            while lt==0:
                if res[1]>r-l:
                    res[0] = s[l:r]
                    res[1] = r-l
                ct = s[l]
                if ct in letter:
                    letter[ct] += 1
                    if letter[ct]>0:
                        lt += 1
                l += 1

        return res[0]



        # lt = len(t)
        # ls = len(s)
        # letter = {}
        # res = [ls+1,ls + 1]
        # temp = 0

        # for i in t:
        #     if i not in letter:
        #         letter[i] = 1
        #     else:
        #         letter[i] += 1
        
        # for i in range(ls):
        #     c = s[i]
        #     if lt:
        #         temp += 1
        #         if c in letter:
        #             letter[c] -= 1
        #             if(letter[c]>=0):
        #                 lt -= 1

        #     while lt==0:
        #         index = i-temp+1
        #         if res[1]>temp:
        #             res = [index,temp]
        #         ct = s[index]
        #         temp -= 1
        #         if ct in letter:
        #             letter[ct] += 1
        #             if letter[ct] == 1:
        #                 lt += 1

        
        # return s[res[0]:res[0]+res[1]] if res[1]!=ls+1 else ""
