class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        v1,v2 = ([*map(int, v.split('.'))] for v in [version1,version2])
        d = len(v1)-len(v2)
        v1 += [0]*(-d)
        v2 += [0]*d
        return (v1>v2)-(v2>v1)


#     def num_convert(self,s):
#         result = 0
#         temp = 0
#         power = 10
#         for i in s:
#             if(i!="."):
#                 temp = temp*10 + int(i)

#             else:
#                 result = result*power + temp
#                 temp = 0
#         return result
    
#     def compareVersion(self, version1: str, version2: str) -> int:
#         l1 = version1.count(".")
#         l2 = version2.count(".")
        
#         if(l1>l2):
#             version2 += ".0"*(l1-l2)
#         else:
#             version1 += ".0"*(l2-l1)
        
#         diff = self.num_convert(version1+".")-self.num_convert(version2+".")
        
#         if(diff>0):
#             return 1
#         elif(diff==0):
#             return 0
#         else:
#             return -1
