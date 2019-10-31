class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result = []
        m1 = {}
        m2 = {}
        for i in nums1:
            if i in m1:
                m1[i]+=1
            else:
                m1[i] = 1
        for j in nums2:
            if j in m1:
                if j in m2:
                    m2[j] += 1
                else:
                    m2[j] = 1

        for i in m2:
            result += [i]*min(m1[i],m2[i])
        return result
        # result = []
        # for i in set.intersection(set(nums1),set(nums2)):
        #     result += [i]*min(nums1.count(i),nums2.count(i))
        # return result
