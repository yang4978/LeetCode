class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        l1 = len(nums1)
        l2 = len(nums2)
        if(l2<l1):
            nums1,nums2,l1,l2 = nums2,nums1,l2,l1
        imin = 0
        imax = l1
        while(imin<=imax):
            i = (imin+imax)//2
            j = (l1+l2)//2-i
            if(i>0 and nums1[i-1]>nums2[j]):
                imax = i-1
            elif(i<l1 and nums2[j-1]>nums1[i]):
                imin = i+1
            else:
                
                if i==0:
                    left_max = nums2[j-1]
                elif j==0:
                    left_max = nums1[i-1]
                else:
                    left_max = max(nums1[i-1],nums2[j-1])
        
                if i==l1:
                    right_min = nums2[j]
                elif j==l2:
                    right_min = nums1[i]
                else:
                    right_min = min(nums1[i],nums2[j])
                
                if (l1+l2)%2:
                    return right_min
                else:
                    return (left_max+right_min)/2.0
        
