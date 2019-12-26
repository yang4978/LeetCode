class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        letter = {}
        num = 0

        for i in s:
            if i not in letter:
                letter[i] = 1
                num += 1
            else:
                letter[i] += 1
        
        for i in t:
            if i not in letter:
                num += 1
            else:
                letter[i] -= 1
                if not letter[i]:
                    num -= 1
        
        return num==0
