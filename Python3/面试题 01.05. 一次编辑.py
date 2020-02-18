class Solution:
    def oneEditAway(self, first: str, second: str) -> bool:
        m = len(first)
        n = len(second)
        
        if abs(m-n)>1:
            return False
        
        i = 0
        j = 0
        count = 0

        while i<m and j<n and count<2:
            if first[i] == second[j]:
                i += 1
                j += 1
            else:
                count += 1
                if m == n:
                    i += 1
                    j += 1
                elif m > n:
                    i += 1
                else:
                    j += 1
            
        return count<2
