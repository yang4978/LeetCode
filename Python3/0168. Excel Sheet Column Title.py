class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        res = ""
        while columnNumber != 0:
            temp = (columnNumber - 1) % 26 + 1
            res = chr(temp - 1 + ord("A")) + res
            columnNumber = (columnNumber - temp) // 26
        
        return res
