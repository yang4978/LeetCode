# class Solution:
#     def checkInclusion(self, s1: str, s2: str) -> bool:
#         c1 = collections.Counter()
#         for i in range(ord('a'),ord('z')+1):
#             c1[chr(i)] = 0
#         print(c1)
#         c2 = c1.copy()

#         l1 = len(s1)
#         l2 = len(s2)

#         for char in s1:
#             c1[char] += 1
        
#         for char in s2[:l1]:
#             c2[char] += 1

#         i = 0
#         j = l1
#         while j < l2:
#             if c1 == c2:
#                 return True
#             c2[s2[i]] -= 1
#             c2[s2[j]] += 1
#             i += 1
#             j += 1
        
#         return c1==c2

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        letter = collections.defaultdict(int)

        for c in s1:
            letter[c] += 1
        
        l = 0
        k = len(s1)
        r = l+k-1
        cnt = k

        if k > len(s2):
            return  False

        for i in range(k):
            if letter[s2[i]] > 0:
                cnt -=1
            letter[s2[i]] -= 1


        while r<len(s2)-1:
            if cnt == 0:
                return True
            l += 1
            r += 1
            
            if letter[s2[l-1]] >= 0:
                cnt += 1
            letter[s2[l-1]] += 1
            
            if letter[s2[r]] > 0:
                cnt -= 1
            letter[s2[r]] -= 1

            
        return False if cnt else True
                

