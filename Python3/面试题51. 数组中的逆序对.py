class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        def mergeSort(arr):
            l = len(arr)
            if l <= 1:
                return arr,0
            left, cl = mergeSort(arr[:l//2])
            right, cr = mergeSort(arr[l//2:])
            res, count = merge(left,right)
            return res, count+cl+cr

        def merge(left,right):
            ll = len(left)
            lr = len(right)

            i, j = 0, 0
            res = []
            count = 0

            while i<ll and j<lr:
                if left[i] <= right[j]:
                    res.append(left[i])
                    i += 1
                else:
                    res.append(right[j])
                    count += ll - i
                    j += 1
            
            res += left[i:] + right[j:]

            return res, count
        
        return mergeSort(nums)[1]
