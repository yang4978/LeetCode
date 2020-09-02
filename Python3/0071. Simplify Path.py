class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []

        for c in path.split('/'):
            if c not in ['','.','..']:
                stack.append(c)
            
            elif c == '..' and stack:
                stack.pop()
        
        return '/' + ('/').join(stack)
