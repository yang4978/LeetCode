class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        # res = []
        # com = [[[],k]]

        # while com:
        #     arr, temp = com.pop()
        #     if temp == 0:
        #         res.append(arr)

        #     if not arr:
        #         start = 0
        #     else:
        #         start = arr[-1]
            
        #     for i in range(start+1,n+1):
        #         com.append([arr+[i],temp-1])

        # return res

        res = [[i] for i in range(1,n+1-k+1)]

        for i in range(k-1,0,-1):
            temp = []
            for j in range(len(res)):
                arr = res.pop()
                for m in range(arr[-1]+1,n+1-i+1):
                    temp.append(arr+[m])
            res = temp[:]       
        return res
