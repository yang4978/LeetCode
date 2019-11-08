class Solution:
    def minimumSwap(self, s1: str, s2: str) -> int:
        l = len(s1)
        letter = [0,0] #s1x,s1y,s2x,s2y
        for i in range(l):
            if(s1[i]!=s2[i]):
                if(s1[i]=='x'):
                    letter[0] += 1
                else:
                    letter[1] += 1
        if((letter[0]+letter[1])%2):
            return -1
        
        else:
            return letter[0]//2+letter[1]//2+letter[0]%2+letter[1]%2
