class Solution:
    def shortestDistance(self, words: List[str], word1: str, word2: str) -> int:
        m = -1
        n = -1
        l = len(words)
        res = l

        for i in range(l):
            if words[i]==word1:
                m = i
            elif words[i]==word2:
                n = i
            
            if m!=-1 and n!=-1:
                res = min(res,abs(m-n))
        
        return res
