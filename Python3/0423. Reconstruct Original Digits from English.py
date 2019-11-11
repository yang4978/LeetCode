class Solution:
    def originalDigits(self, s: str) -> str:
        letter = collections.Counter(s)
        digit = {}
        res = ''
        digit['0'] = letter['z']
        digit['2'] = letter['w']
        digit['4'] = letter['u']
        digit['6'] = letter['x']
        digit['8'] = letter['g']
        digit['3'] = letter['t'] - digit['8'] - digit['2']
        digit['5'] = letter['f'] - digit['4']
        digit['7'] = letter['v'] - digit['5']
        digit['9'] = letter['i'] - digit['5'] - digit['8'] - digit['6']
        digit['1'] = letter['o'] - digit['0'] - digit['2'] - digit['4']
        
        for i in range(10):
            res += digit[str(i)]*str(i)
        
        return res
        
#         digit = {}
#         for i in range(10):
#             digit[str(i)] = 0
#         res = ''
        
#         letter = collections.Counter(s)
        
#         num = {'z':['0','e','r','o'],'w':['2','t','o'],'u':['4','f','o','r'],'f':['5','i','v','e'],'x':['6','s','i'],'g':['8','e','i','h','t'],'r':['3','t','h','e','e'],'v':['7','s','e','e','n'],'i':['9','n','n','e'],'n':['1','o','e']}
        
#         for i,j in num.items():
#             digit[j[0]] += letter[i]
#             for k in j[1:]:
#                 letter[k] -= letter[i]
#             letter[i] = 0
        
#         for i,j in digit.items():
#             res += j*i
        
#         return res
