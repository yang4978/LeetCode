class Solution:
    def judgeCircle(self, moves: str) -> bool:
        vertical = 0
        horizon = 0
        for c in moves:
            if c == 'U':
                vertical += 1
            elif c == 'D':
                vertical -= 1
            elif c == 'L':
                horizon -= 1
            else:
                horizon += 1
        
        return vertical == 0 and horizon == 0
