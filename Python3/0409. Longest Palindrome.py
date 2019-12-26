class Solution:
    def longestPalindrome(self, s: str) -> int:
        letter = collections.defaultdict(int)

        for c in s:
            letter[c] += 1
        
        return sum(i//2*2 for i in letter.values())+int(sum(i%2 for i in letter.values())>0)
