class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        letter = {}
        l = len(s)
        temp = 0
        char = 0
        res = 0
        
        left,right = 0,0
        while right < l:
            if s[right] not in letter:
                char += 1
                letter[s[right]] = 1
            else:
                letter[s[right]] += 1
            
            temp += 1

            if char<=2:
                if temp>res:
                    res = temp
            else:
                while char>2:
                    letter[s[left]] -= 1
                    if letter[s[left]] == 0:
                        del letter[s[left]]
                        char -= 1
                    temp -= 1
                    left += 1

            right += 1

        return res
