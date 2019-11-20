class Solution:
    def countPrimeSetBits(self, L: int, R: int) -> int:
        prime = [0, 0, 1, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1]
        return sum(prime[bin(i).count('1')] for i in range(L,R+1))

        # prime = [0, 0, 1, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1]
        # binary = []
        # num = 0
        # res = 0
        # a = L
        # l = 0
        # while(a):
        #     binary.append(a%2)
        #     num += a%2
        #     a //= 2
        #     l += 1
        # res += prime[num]

        # while L<R:
        #     L += 1
        #     flag = 1
        #     for i in range(l):
        #         binary[i] += flag
        #         if(binary[i]==2):
        #             binary[i] = 0
        #             flag = 1
        #             num -= 1
        #         else:
        #             flag = 0
        #             num += 1
        #             break
        #     if(flag):
        #         binary.append(1)
        #         l += 1
        #         num += 1

        #     res += prime[num]

        # return res
