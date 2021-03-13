# If you need to import additional packages or classes, please import here.

def func():
    # please define the python3 input here. 
    # For example: a,b = map(int, input().strip().split())
    # please finish the function body here.
    # please define the python3 output here. For example: print().
    while True:
        try:
            n,m = map(int,input().strip().split())
            arr = list(map(int,input().strip().split()))
            print(sum(1 if i>=arr[m-1] and i>0 else 0 for i in arr))
        except EOFError:
            break
    
if __name__ == "__main__":
    func()
