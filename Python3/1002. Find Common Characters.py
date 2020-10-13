class Solution:
    def commonChars(self, A: List[str]) -> List[str]:
        num = collections.defaultdict(int)
        letter = set(A[0])
        for c in letter:
            num[c] = A[0].count(c)
        

        for s in A[1:]:
            for c in letter:
                num[c] = min(num[c],s.count(c))
        
        res = []

        for c in num:
           res += [c] * num[c]

        return res 
