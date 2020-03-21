class Solution:
    def toHexspeak(self, num: str) -> str:
        num = int(num)
        res = ""
        letter = {10:'A',11:'B',12:'C',13:'D',14:'E',15:'F',1:'I',0:'O'}
        while num:
            if 2<=num%16<=9:
                return "ERROR"
            else:
                res += letter[num%16]
                num //= 16
        
        return ''.join(reversed(res))
