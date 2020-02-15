class Solution:
    def CheckPermutation(self, s1: str, s2: str) -> bool:
        letter = {}
        for s in s1:
            letter[s] = letter.get(s,0) + 1
        
        for s in s2:
            if letter.get(s,0) == 0:
                return False
            letter[s] -= 1
        
        return True
