class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        xor = 0
        x = 0
        y = 0
        for i in nums:
            xor ^= i
        
        xor &= ~xor+1
        
        for i in nums:
            if(xor&i==0):
                x ^= i
            else:
                y^= i
        return x,y
