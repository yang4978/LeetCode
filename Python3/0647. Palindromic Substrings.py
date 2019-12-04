class Solution:
    def countSubstrings(self, s: str) -> int:
        l = 2*len(s)+1
        p = [0]*l
        ss = "#"
        for c in s:
            ss += c+'#'
        
        center = 0
        right = 0
        res = 0
        
        for i in range(1,l):
            p[i] = min(p[2*center-i],right-i+1) if right>i else 1

            while i+p[i]<l and i-p[i]>=0 and ss[i+p[i]]==ss[i-p[i]]:
                p[i] += 1
            
            if p[i]+i-1>right:
                center = i
                right =p[i]+i-1

            res += p[i]//2
        return res


########中心扩散法########

        # l = len(s)
        # res = l

        # for i in range(l-1):
        #     k = 1
        #     while i-k>=0 and i+k<l and s[i-k]==s[i+k]:
        #         res += 1
        #         k += 1
            
        #     if s[i]==s[i+1]:
        #         k = 0
        #         while i-k>=0 and i+1+k<l and s[i-k] == s[i+k+1]:
        #             res += 1
        #             k += 1
        
        # return res

######## BFS ##########

        # def  isPalidromic(s):
        #     l = len(s)
        #     return s[:l//2]==s[:(l-1)//2:-1]
        
        # queue = []
        # res = 0
        # l = len(s)
        # for i in range(l):
        #     queue.append((s[i],i))

        # while queue:
        #     temp,index = queue.pop(0)
        #     res += isPalidromic(temp)

        #     if index+1<l:
        #         queue.append((temp+s[index+1],index+1))
            

        # return res
