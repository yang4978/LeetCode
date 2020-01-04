class Solution:
    def pathInZigZagTree(self, label: int) -> List[int]:
        res = []
        while label!=1:
            res.append(label)
            label >>= 1
            label = label^((1<<(label.bit_length()-1))-1)
            # label = label^(1<<(label.bit_length()-1)) - 1
        return [1]+res[::-1]


        # digit = []
        # while label:
        #     digit.append(1-label%2)
        #     label //= 2
        
        # digit.reverse()

        # res = []
        # flag = 1-len(digit)%2
        # pos = 0
        # layer = 0


        # for i in digit:
        #     pos = pos*2 + i
        #     if flag:
        #         res.append(2**layer+pos)
        #         flag = 0
        #     else:
        #         res.append(2**(layer+1)-1-pos)
        #         flag = 1
        #     layer += 1
        
        # return res
