class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        count = 0
        l = len(flowerbed)

        for i in range(l):
            if flowerbed[i]==0 and (i==0 or flowerbed[i-1]==0) and (i==l-1 or flowerbed[i+1]==0):
                flowerbed[i] = 1
                count += 1
        
        return n<=count

        # res = 0
        # temp = 0

        # flowerbed = [0]+flowerbed+[0]

        # for i in flowerbed:
        #     if i:
        #         res += max(0,(temp-1)//2)
        #         temp = 0
        #     else:
        #         temp += 1

        # res += max(0,(temp-1)//2)

        # return n<=res
