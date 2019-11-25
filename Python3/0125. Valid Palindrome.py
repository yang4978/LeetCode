class Solution:
    def isPalindrome(self, s: str) -> bool:
        temp = ''
        for i in s:
            if i.isalnum():
                temp += i.lower()
        
        # i,j = 0,len(temp)-1
        # while(i<j):
        #     if temp[i]!=temp[j]:
        #         return False
        #     else:
        #         i += 1
        #         j -= 1
        # return True
        return temp==temp[::-1]

#         s = s.lower()
#         i = 0
#         j = len(s)-1
#         while(i<j):
#             while i<j and not s[i].isalnum():
#                 i += 1
#             while i<j and not s[j].isalnum():
#                 j -= 1
#             if s[i]!=s[j]:
#                 return False
#             i += 1
#             j -= 1
        
#         return True
