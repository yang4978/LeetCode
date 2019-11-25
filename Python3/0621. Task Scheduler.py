class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        if n==0:
            return len(tasks)
        arr = [0]*26
        for i in tasks:
            arr[ord(i)-ord('A')] += 1
        
        res = (max(arr)-1)*(n+1)+arr.count(max(arr))

        return res if res>len(tasks) else len(tasks)

#         if n==0:
#             return len(tasks)
#         arr = [0]*26
#         for i in tasks:
#             arr[ord(i)-ord('A')] += 1
#         arr.sort()

#         res = 0
#         while(max(arr)>1):
#             t = 0
#             j = len(arr)-1
#             while(j>-1 and t<n+1):
#                 if(arr[j]):
#                     arr[j] -= 1
#                     t += 1
#                 j -= 1
#             res += n+1
#             arr.sort()

#         return res+sum(arr)

