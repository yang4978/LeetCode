class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = {'a','e','i','o','u','A','E','I','O','U'}
        s = list(s)

        l = len(s)
        i = 0
        j = l-1

        while i<j:
            while i<j and s[i] not in vowels:
                i += 1
            
            while i<j and s[j] not in vowels:
                j -= 1
            
            if i>j:
                break

            s[i],s[j] = s[j],s[i]
            i += 1
            j -= 1
        
        return "".join(s)
