class Solution:
    def validWordSquare(self, words: List[str]) -> bool:
        m = len(words)
    
        for i in range(m):
            l = len(words[i])
            if l > m:
                return False
            words[i] = words[i] + ' '*(m-l)

        for i in range(m):
            for j in range(i+1,m):
                if words[i][j] != words[j][i]:
                    return False
        
        return True
