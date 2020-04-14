class Solution:
    def smallestDifference(self, a: List[int], b: List[int]) -> int:
        # total = {}
        # seq = {}

        # for i in set(a):
        #     total[i] = -1
        
        # for i in set(b):
        #     if i in total:
        #         return 0
        #     total[i] = 1
        
        # arr = sorted(total.keys())
        # for i in range(len(total)):
        #     seq[arr[i]] = i
        
        # temp = [total[i] for i in arr]
        # res = float('inf')
        # for i in range(1,len(total)):
        #     if temp[i-1]*temp[i] < 0:
        #         res = min(res,arr[i]-arr[i-1])
        
        # return res

        a.sort()
        b.sort()
        la = len(a)
        lb = len(b)
        i = 0
        j = 0
        res = float('inf')

        while i<la and j<lb:
            res = min(res,abs(a[i]-b[j]))
            if a[i]>b[j]:
                j += 1
            else:
                i += 1
        
        return res
