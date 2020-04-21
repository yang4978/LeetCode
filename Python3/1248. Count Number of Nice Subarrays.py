class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        zero = []
        t = 0
        for i in nums:
            if i%2:
                zero.append(t)
                t = 0
            else:
                t += 1
        zero.append(t)
        return sum((1+zero[k+i])*(1+zero[i]) for i in range(len(zero)-k))
