class Solution:
    def reverseWords(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        l = len(s)
        s.reverse()
        last = 0

        for i in range(l+1):
            if i == l or s[i] == ' ':
                length = i - last + 1

                for k in range(length//2):
                    s[last+k], s[i-k-1] = s[i-k-1], s[last+k] 

                last = i + 1
        
    
