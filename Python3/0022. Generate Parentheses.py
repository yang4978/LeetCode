class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        temp = [[""]]
        for i in range(1,n+1):
            temp_set = set()
            for j in range(i):  
                for arr1 in temp[j]:
                    for arr2 in temp[i-j-1]:
                        temp_set.add("("+arr1+")"+arr2)
            if(i!=n):
                temp.append(list(temp_set))
            else:
                return list(temp_set)

#         res = set()
#         deque = [["(",n-1,n]]
#         while(len(deque)!=0):
#             temp_str,left,right = deque.pop()

#             if(left==0 and right==0 and len(deque)):
#                 res.add(temp_str)
#                 temp_str,left,right = deque.pop()
            
#             if(left>0):
#                 deque.append([temp_str+"(",left-1,right])
#             if(right>0 and left<right):
#                 deque.append([temp_str+")",left,right-1])
#         res.add(temp_str)
#         return list(res)
