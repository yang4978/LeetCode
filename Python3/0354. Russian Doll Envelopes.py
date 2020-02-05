class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        l = len(envelopes)

        if l<2:
            return l

        envelopes.sort(key = lambda x:(x[0],-x[1]))

        dp = []
        res = 0

        for i in range(l):
            num = envelopes[i][1]
            left = 0
            right = res

            while left < right:
                mid = (left+right)>>1
                if dp[mid] < num:
                    left = mid + 1
                else:
                    right = mid
            
            if left == res:
                dp.append(num)
                res += 1
            else:
                dp[left] = num
        
        return res
