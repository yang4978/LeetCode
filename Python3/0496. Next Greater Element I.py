class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ele = {}
        stack = []
        for i in nums2:
            while stack and i>stack[-1]:
                ele[stack.pop()] = i
            stack.append(i)
        
        while stack:
            ele[stack.pop()] = -1
        
        return [ele[i] for i in nums1]
