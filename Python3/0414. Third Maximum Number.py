class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        nums = list(set(nums))
        stack = nums[:3]
        stack.sort()
        for i in nums[3:]:
            if i >= stack[0]:
                if i<stack[1]:
                    stack[0] = i
                elif i>=stack[1]:
                    if i<stack[2]:
                        stack[0],stack[1] = stack[1],i
                    else:
                        stack.pop(0)
                        stack.append(i)
        
        return stack[0] if len(stack)==3 else stack[-1]
