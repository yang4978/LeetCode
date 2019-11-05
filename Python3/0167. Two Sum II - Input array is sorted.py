class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # num_dict = {}
        # for i in range(len(numbers)):
        #     if numbers[i] not in num_dict:
        #         num_dict[target-numbers[i]] = i
        #     else:
        #         return [num_dict[numbers[i]]+1,i+1]
        i,j = 0,len(numbers)-1
        while(i<j):
            if(numbers[i]+numbers[j]<target):
                i += 1
            elif(numbers[i]+numbers[j]>target):
                j -= 1
            else:
                return [i+1,j+1]
