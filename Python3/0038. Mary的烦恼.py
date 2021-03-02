# If you need to import additional packages or classes, please import here.

def func():
    # please define the python3 input here. 
    # For example: a,b = map(int, input().strip().split())
    # please finish the function body here.
    # please define the python3 output here. For example: print().
    while True:
        try:
            n, pack = map(int,input().strip().split())
            arr = list(map(int,input().strip().split()))
            used = [0]*n
            
            def dfs(rest,index,used):
                if rest == 0:
                    return True
                if sum(used)==n:
                    return False
                for i in range(index,n):
                    if used[i] == 0 and rest >= arr[i]:
                        used[i] = 1
                        if dfs(rest-arr[i],i+1,used):
                            return True
                        used[i] = 0
                return False
            flag = 0
            for i in range(n):
                used[i] = 1
                if dfs(pack-arr[i],i+1,used):
                    print("YES")
                    flag = 1
                    break
                used[i] = 0
            if flag==0:
                print("NO")
        except EOFError:
            break

    
if __name__ == "__main__":
    func()
