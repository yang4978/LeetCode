class Window:
    def __init__(self):
        self.num = collections.Counter()
        self.non_dup = 0
        
    def add(self,s):
        self.num[s] += 1
        if self.num[s]==1 :
            self.non_dup += 1
            
    def sub(self,s):
        self.num[s] -= 1
        if self.num[s]==0 :
            self.non_dup -= 1

class Solution:
    def subarraysWithKDistinct(self, A: List[int], K: int) -> int:
        W1 = Window()
        W2 = Window()
        l1=l2=ans = 0
        
        
        for x in A:
            W1.add(x)
            W2.add(x)
            
            while W1.non_dup >K : 
                W1.sub(A[l1])
                l1 += 1
            while W2.non_dup >= K:
                W2.sub(A[l2])
                l2 += 1
            
            ans += l2-l1
        return ans
