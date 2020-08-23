class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        # def gcd(x, y):
        #     if x < y:
        #         y, x = x, y
            
        #     while x % y:
        #         x, y = y, x%y
                
        #     return y

        # char = collections.defaultdict(int)

        # l = len(s)

        # for c in s:
        #     char[c] += 1

        # num = min(char.values())

        # for i in char.values():
        #     num = gcd(num,i)    
        #     if num == 1:
        #         return False

        # if s == s[:l//num]*(num):
        #     return True
        

######################################################################################

        # for i in range(2,int(math.sqrt(l))):
        #     if num%i == 0:
        #         if (num!=i and s == s[:l//(num//i)]*(num//i)) or s == s[:l//i]*i:
        #             return True
        
        # return False


######################################################################################

        return (s+s).find(s,1)!=len(s)
