class Solution:
    def beautifulArray(self, N: int) -> List[int]:
        res = [1]

        count = 1
        while(count<N):
            res = [i*2-1 for i in res] + [i*2 for i in res]
            count = count*2
        
        res = [i for i in res  if i<=N]

        return res
