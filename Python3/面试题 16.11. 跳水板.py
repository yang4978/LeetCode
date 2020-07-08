class Solution:
    def divingBoard(self, shorter: int, longer: int, k: int) -> List[int]:
        return [] if k==0 else [(k-i)*shorter+i*longer for i in range(k+1)] if shorter!=longer else [k*shorter]
