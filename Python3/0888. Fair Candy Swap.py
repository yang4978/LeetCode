class Solution:
    def fairCandySwap(self, A: List[int], B: List[int]) -> List[int]:
        diff = (sum(A)-sum(B))//2
        setB = set(B)
        for i in A:
            if i-diff in setB:
                return [i,i-diff]
