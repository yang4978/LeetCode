class Solution:
    def fixedPoint(self, A: List[int]) -> int:
        # for i in range(len(A)):
        #     if i==A[i]:
        #         return i
        # return -1

        left = 0
        right = len(A)-1

        while left<=right:
            mid = left + (right-left)//2
            if A[mid]<mid:
                left = mid + 1
            elif A[mid]>=mid:
                right = mid - 1
            if mid>=len(A)-1:
                return -1
        
        return left if A[left]==left else -1

        # left = 0
        # right = len(A)-1

        # while left<right:
        #     mid = left + (right-left)//2
        #     if A[mid]<mid:
        #         left = mid+1
        #     elif A[mid]>=mid:
        #         right = mid
        
        # return left if A[left]==left else -1
