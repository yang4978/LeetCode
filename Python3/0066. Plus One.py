class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits[-1] += 1
        flag = 0
        for i in range(len(digits)-1,-1,-1):
            digits[i],flag = (digits[i]+flag)%10,(digits[i]+flag)//10
        if(flag):
            digits.insert(0,flag)
        return digits
