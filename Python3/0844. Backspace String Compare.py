class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        
        def generateNewString(string):
            stack = []
            for c in string:
                if c == '#':
                    if stack:
                        stack.pop()
                else:
                    stack.append(c)
        
            return stack

        return generateNewString(S) == generateNewString(T)
