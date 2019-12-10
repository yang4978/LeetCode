class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 0:
            return []
        res = [[1]]
        while numRows>1:
            t1 = res[-1]+[0]
            t2 = [0]+res[-1]
            res.append([t1[i]+t2[i] for i in range(len(t1))] )
            numRows -= 1
        
        return res
