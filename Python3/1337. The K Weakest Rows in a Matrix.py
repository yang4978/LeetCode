class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        l = len(mat)
        arr = [i for i in range(l)]
        arr.sort(key = lambda x:sum(mat[x]))
        return arr[:k]
