class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        residual = collections.defaultdict(int)
        res = 0
        for i in time:
            mod = i%60
            diff = 60-mod if mod else 0
            res += residual[diff]
            residual[mod] += 1
        
        return res

        # residual = {}
        # res = 0
        # for i in time:
        #     mod = i%60
        #     diff = 60-mod if mod else 0
        #     if diff in residual:
        #         res += residual[diff]
        #     if mod not in residual:
        #         residual[mod] = 1
        #     else:
        #         residual[mod] += 1
        
        # return res
