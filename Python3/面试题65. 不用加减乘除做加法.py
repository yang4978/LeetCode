class Solution:
    def add(self, a: int, b: int) -> int:
        a &= 0xffffffff
        b &= 0xffffffff

        while b != 0:
            carry = ((a&b)<<1)&0xffffffff
            a ^= b
            b = carry
        
        return a if a < 0x80000000 else ~(a^0xffffffff)
