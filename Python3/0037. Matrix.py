# If you need to import additional packages or classes, please import here.

def func():
    # please define the python3 input here. 
    # For example: a,b = map(int, input().strip().split())
    # please finish the function body here.
    # please define the python3 output here. For example: print().
    while True:
        try:
            n,m = map(int,input().strip().split())
            res = []
            for _ in range(n):
                temp = list(map(int,input().strip().split()))
                res.append(temp)
                
            for j in range(1,m):
                res[0][j] += res[0][j-1]

            for i in range(1,n):
                res[i][0] += res[i-1][0]

            for i in range(1,n):
                for j in range(1,m):
                    res[i][j] += max(res[i-1][j],res[i][j-1])

            print(res[-1][-1])


        except EOFError:
            break
    

    
if __name__ == "__main__":
    func()
