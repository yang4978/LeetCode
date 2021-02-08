class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        l1 = len(nums1)
        l2 = len(nums2)

        if l1 == 0 or l2 == 0:
            return []

        add = collections.defaultdict(list)

        for i in range(l1):
            add[nums1[i]+nums2[0]].append([i,0])
        
        res = []

        while k and len(add):
            temp = min(add)
            arr = add[temp].pop(0)
            i1,i2 = arr
            res.append([nums1[i1],nums2[i2]])
            if not add[temp]:
                del add[temp]
            if i2 + 1 < l2:
                add[nums1[i1]+nums2[i2+1]].append([i1,i2+1])
            k -= 1
        
        return res
