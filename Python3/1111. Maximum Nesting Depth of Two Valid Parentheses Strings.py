class Solution:
    def maxDepthAfterSplit(self, seq: str) -> List[int]:
        result = []
        a, b = 0, 0
        for i in seq:
            if i == '(':
                if a<b:
                    a += 1
                    result.append(0)
                else:
                    b += 1
                    result.append(1)
            else:
                if a>b:
                    a -= 1
                    result.append(0)
                else:
                    b -= 1
                    result.append(1)
        return result
