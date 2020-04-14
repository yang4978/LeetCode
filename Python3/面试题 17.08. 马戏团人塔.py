class Solution:
    def bestSeqAtIndex(self, height: List[int], weight: List[int]) -> int:
        index = defaultdict(list)

        for i,h in enumerate(height):
            index[h].append(weight[i])

        arr = []
        for i in sorted(index.keys()):
            arr += sorted(index[i],reverse=True)

        dp = []

        for x in arr:
            # left = bisect.bisect_left(dp,x)
            l = len(dp)

            left = 0
            right = l

            while left < right:
                mid = (left+right)//2
                if dp[mid] < x:
                    left = mid + 1
                else:
                    right = mid

            if left == l:
                dp.append(x)
            else:
                dp[left] = x

        return len(dp)
