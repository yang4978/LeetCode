class Solution:
    def grayCode(self, n: int) -> List[int]:
        if n==0:
            return [0]
        
        arr = self.grayCode(n-1)
        
        return arr + [arr[i]+pow(2,n-1) for i in range(pow(2,n-1)-1,-1,-1)]
