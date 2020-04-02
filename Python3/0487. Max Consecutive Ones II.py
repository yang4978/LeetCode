class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        # seq = []
        # temp = 0

        # for i in nums:
        #     if i == 0:
        #         if temp:
        #             seq.append(temp)
        #             temp = 0
        #         seq.append(0)
        #     else:
        #         temp += 1

        # if temp:
        #     seq.append(temp)
        # l = len(seq)

        # return (1 + max(seq[i]+seq[i+1]+seq[i+2] for i in range(l-2))) if l>=3 else sum(seq) + int(0 in seq)

        res = 0
        dp0, dp1 = 0, 0

        for i in nums:
            if i:
                dp0 += 1
                dp1 += 1
            else:
                dp1 = dp0 + 1
                dp0 =0
            res = max(res,dp1,dp0)

        return res
