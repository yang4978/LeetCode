class Solution:
    def intToRoman(self, num: int) -> str:
        res = ""
        number =[1,4,5,9,10,40,50,90,100,400,500,900,1000] 
        letter =["I","IV","V","IX","X","XL","L","XC","C","CD","D","CM","M"]
        index = 12
        while(num):
            if(num>=number[index]):
                num -= number[index]
                res += letter[index]
            else:
                index -= 1
        return res
#         res = ""
#         letter = {1:"I",4:"IV",5:"V",9:"IX",10:"X",40:"XL",50:"L",90:"XC",100:"C",400:"CD",500:"D",900:"CM",1000:"M"}
#         power = 1
#         while(num):
#             temp = num%10*power
#             if(temp in letter):
#                 res = letter[temp] + res
#             else:
#                 flag = 0
#                 if(temp>=5*power):
#                     temp -= 5*power
#                     flag = 1
#                 while(temp):
#                     temp -= power
#                     res = letter[power] + res
#                 if(flag):
#                     res = letter[5*power] + res
                    
#             power *= 10
#             num //= 10
#         return res
