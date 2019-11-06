class Solution:
    def decodeAtIndex(self, S: str, K: int) -> str:
        l = 0
        for i in S:
            if('2'<=i<='9'):
                l=int(i)*l
            else:
                l += 1
        
        for i in reversed(S):
            K %= l
            if K==0 and i.isalpha():
                return i
            else:
                if '2'<=i<='9':
                    l //= int(i)
                else:
                    l -= 1
