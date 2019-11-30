class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        # l = s.strip().split(" ")
        # return len(l[-1]) if l!=[] else 0
        return len(s.strip().split(" ")[-1])
