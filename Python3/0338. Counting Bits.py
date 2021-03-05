class Solution(object):
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
#         res = [0]*(num+1)

#         for i in range(1,num+1):
#             res[i] = (res[i-1]+1) if i%2 else res[i//2]
        
#         return res

        # res = [0]*(num+1)

        # mask = 1
        # while(mask<=num):
        #     for i in range(1,num+1):
        #         res[i] += (mask&i)!=0
        #     mask <<= 1

        # return res
        
        arr = [0]
        bit = 1
        while((1<<bit)<num):
            bit += 1
        for i in range(1,bit+1):
            for j in range(1<<(i-1)):
                arr.append(1+arr[j])
        return arr[:num+1] if len(arr)>num else arr+[1]
