class Solution:
    def partitionDisjoint(self, A: List[int]) -> int:
        l_max = A[0]
        r_min = min(A[1:])

        for i in range(1,len(A)):
            if l_max <= r_min:        # 左边最小值 <= 右边最大值，此时下标i即为左边的长度
                return i
            l_max = max(A[i],l_max)
            if A[i]==r_min:
                r_min = min(A[i+1:])
