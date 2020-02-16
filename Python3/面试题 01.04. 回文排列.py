class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        letter = {}

        for c in s:
            letter[c] = letter.get(c,0) + 1
        
        return sum(i%2 for i in letter.values())<=1
