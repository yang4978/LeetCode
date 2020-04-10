class Solution:
    def similarRGB(self, color: str) -> str:
        # res = '#'
        # for i in range(1,7,2):
        #     res += hex((int(color[i:i+2],16)+8)//17)[2:]*2
        # return res

        return '#' + ''.join([hex((int(color[i:i+2],16)+8)//17)[2:]*2 for i in range(1,7,2)])

        # res = "#"
        # for i in range(1,7,2):
        #     s1 = color[i:i+2]
        #     pair = [float('inf'),""]
        #     s2 = []
        #     if s1[0]!='0' and s1[0]!='a':
        #         s2.append(chr(ord(s1[0])-1)*2)

        #     if s1[0] == 'a':
        #         s2.append('99')

        #     s2.append(s1[0]*2)

        #     if s1[0]!='f' and s1[0]!='9':
        #         s2.append(chr(ord(s1[0])+1)*2)
            
        #     if s1[0] == '9':
        #         s2.append('aa')
            
        #     for ss in s2:
        #         t = abs(int(s1,16)-int(ss,16))
        #         if t < pair[0]:
        #             pair = [t,ss]
        #     res += pair[1]
        # return res
