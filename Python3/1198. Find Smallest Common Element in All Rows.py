class Solution:
    def smallestCommonElement(self, mat: List[List[int]]) -> int:
        s = set(mat[0])
        
        for i in mat[1:]:
            s = s & set(i)

        return min(list(s)) if s else -1
