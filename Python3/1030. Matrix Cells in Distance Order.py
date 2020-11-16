class Solution:
    def allCellsDistOrder(self, R: int, C: int, r0: int, c0: int) -> List[List[int]]:
        rigid = [[x,y] for x in range(R) for y in range(C)]
        rigid.sort(key = lambda x:abs(x[0]-r0)+abs(x[1]-c0))
        return rigid
