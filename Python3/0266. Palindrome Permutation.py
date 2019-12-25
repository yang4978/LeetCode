class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        char = collections.defaultdict(int)

        for i in s:
            char[i] += 1
        
        return sum(i%2 for i in char.values())<=1
