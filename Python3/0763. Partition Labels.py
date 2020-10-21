class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        end = dict()
        l = len(S)
        
        for i in range(l-1,-1,-1):
            c = S[i]
            if c not in end:
                end[c] = i
        
        i = 0
        result = []

        while i < l:
            p_start = i
            p_end = end[S[i]]
            temp_end = p_end
            flag = 1 
            while flag:
                for c in set(S[p_start:p_end+1]):
                    temp_end = max(temp_end,end[c])
                
                if temp_end == p_end:
                    result.append(p_end + 1 - p_start)
                    i = p_end + 1
                    flag = 0
                else:
                    p_end = temp_end
        
        return result
                
