class Solution:
    def subarraysDivByK(self, A: List[int], K: int) -> int:
        record = {0:1}
        total, res = 0, 0

        for i in A:
            total += i
            mod = total%K
            same = record.get(mod,0)
            res += same
            record[mod] = same+1
        
        return res 
