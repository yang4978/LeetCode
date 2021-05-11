class Solution:
    def decode(self, encoded: List[int]) -> List[int]:
        num0 = 0
        num1 = 0

        for i in range(1, len(encoded) + 2):
            num0 ^= i
        
        for i in range(1, len(encoded) + 1, 2):
            num1 ^= encoded[i]
        
        num0 ^= num1

        arr = [num0]

        for x in encoded:
            arr.append(x ^ arr[-1])
        
        return arr
