class Solution:
    def flipAndInvertImage(self, A: List[List[int]]) -> List[List[int]]:
        return [reversed([i^1 for i in arr]) for arr in A]
