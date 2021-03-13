# If you need to import additional packages or classes, please import here.

def func():
    # please define the python3 input here. 
    # For example: a,b = map(int, input().strip().split())
    # please finish the function body here.
    # please define the python3 output here. For example: print().
    while True:
        try:
#             n = int(input())
#             fac = [1]*((n+1)//2+1)
#             for i in range(1,(n+1)//2+1):
#                 fac[i] = fac[i-1]*(n-2*i+2)*(n-2*i+1)//(2*i-1)//(2*i)
#             res = 0
#             for i in range(0,n+1,2):
#                 res += fac[i//2]*pow(2,(n-i))
#             print(res)
            
            n = int(input())
            print((pow(3,n)+1)//2)
        
        except EOFError:
            break
    
if __name__ == "__main__":
    func()
