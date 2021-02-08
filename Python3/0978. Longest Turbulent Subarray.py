class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        l = len(arr)
        if l <= 1:
            return l
        i = 0
        j = 1
        while j < l and arr[i] == arr[j]:
            i += 1
            j += 1

        res = 1
        
        if j<l:
            flag = 1 if arr[i] < arr[j] else -1
            res = 2

        while j < l:
            if flag * arr[j-1] > flag * arr[j]:
                flag *= -1
                res = max(res,j-i+1)
            else:
                i = j - 1
                while j < l and arr[i] == arr[j]:
                    i += 1
                    j += 1
                if j<l:
                    flag = 1 if arr[i] < arr[j] else -1
            j += 1
        
        return res
