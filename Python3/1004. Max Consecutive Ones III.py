class Solution:
    def longestOnes(self, A: List[int], K: int) -> int:
        res = 0
        num_k = 0
        diff = 0
        temp_sum = 0
        cir = [0]

        for i in A:
            if i == 0:
                cir.append(diff)
                num_k += 1
                diff = 0
                if num_k >= K:
                    res = max(res,temp_sum + K)
                    temp_sum -= cir[num_k-K]
            else:
                diff += 1
                temp_sum += 1 

        if num_k < K:
            res = temp_sum + num_k
        else:
            res = max(res,temp_sum + K)

        return res

