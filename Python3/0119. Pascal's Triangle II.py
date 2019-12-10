class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        # res = [[1]]
        # while rowIndex:
        #     t1 = res[-1]+[0]
        #     t2 = [0]+res[-1]
        #     res.append([t1[i]+t2[i] for i in range(len(t1))] )
        #     rowIndex -= 1
        
        # return res[-1]
        
        res = [1]

        for _ in range (rowIndex):
            res = [1] + [res[i]+res[i+1] for i in range(len(res)-1)] + [1]

        return res
