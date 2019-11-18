class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        res = []
        lp = len(p)

        if(lp>len(s)):
            return []

        letter = {}

        for i in p:
            if i not in letter:
                letter[i] = 0
            letter[i] += 1
        
        count = 0
        for i in range(lp):
            if s[i] in letter:
                letter[s[i]] -= 1
                if letter[s[i]]>=0:
                    count += 1
        
        if(count==lp):
            res.append(0)

        for i in range(len(s)-lp):
            if s[i] in letter:
                letter[s[i]] += 1
                if(letter[s[i]]>0):
                    count -= 1
            
            if s[i+lp] in letter:
                letter[s[i+lp]] -= 1
                if(letter[s[i+lp]]>=0):
                    count += 1
            
            if count==lp:
                res.append(i+1)
            
        return res


        # lp = len(p)
        # if(lp>len(s)): return []

        # res = []
        # letter = collections.defaultdict(int)
        # for i in p:
        #     letter[i] += 1

        # for i in range(lp):
        #     letter[s[i]] -= 1
        
        # if min(letter.values())==0:
        #         res.append(0)
        
        # for i in range(0,len(s)-lp):
        #     letter[s[i]] += 1
        #     letter[s[i+lp]] -= 1

        #     if min(letter.values())==0:
        #         res.append(i+1)
        
        # return res
