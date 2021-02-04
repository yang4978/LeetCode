class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        def median(arr):
            l = len(arr)
            if l%2:
                return arr[l//2]
            else:
                return (arr[l//2]+arr[l//2-1])/2

        l = 0
        r = k-1
        arr = sorted(nums[:k])

        res = [median(arr)]
        while r < len(nums)-1:
            old_num = nums[l]
            #arr.remove(old_num)

            left = 0
            right = k
            while left < right:
                m = (left+right)//2
                if old_num <= arr[m]:
                    right = m
                else:
                    left = m + 1
            arr.pop(left)

            l += 1
            r += 1
            new_num = nums[r]

            left = 0
            right = k-1
            while left<right:
                m = (left+right)//2
                if new_num <= arr[m]:
                    right = m
                else:
                    left = m + 1
            arr.insert(left,new_num)

            last_median = res[-1]
            res.append(median(arr))

        return res

