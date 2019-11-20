class Solution:
    def readBinaryWatch(self, num: int) -> List[str]:
        def digit(n):
            res = 0
            while n:
                res += n%2
                n //= 2
            return res

        res = []
        h = collections.defaultdict(list)
        m = collections.defaultdict(list)

        for i in range(12):
            h[digit(i)].append(str(i))

        for j in range(60):
            m[digit(j)].append((j<10)*'0'+str(j))

        for i in range(num+1):
            for hour in h[i]:
                for minute in m[num-i]:
                    res.append(hour+':'+minute)
        
        return res

        # def digit(n):
        #     res = 0
        #     while n:
        #         res += n%2
        #         n //= 2
        #     return res

        # res = []
        # for i in range(12):
        #     for j in range(60):
        #         if digit(i)+digit(j)==num:
        #             res.append(str(i)+':'+(j<10)*'0'+str(j))
        
        # return res


        # hour = [1,2,4,8]
        # minute = [1,2,4,8,16,32]
        # res = []

        # def dfs(index,arr,temp,r_arr,l,limit,used):
        #     if l==0 and temp<limit:
        #         r_arr.append(str(temp))
            
        #     for i in range(index,len(arr)):
        #         if not used[i]:
        #             temp += arr[i]
        #             used[i] = True
        #             l -= 1
        #             dfs(i+1,arr,temp,r_arr,l,limit,used)
        #             temp -= arr[i]
        #             used[i] = False
        #             l += 1
            


        # for i in range(num+1):
        #     h = []
        #     used_h = [False]*4
        #     m = []
        #     used_m = [False]*6

        #     dfs(0,hour,0,h,i,12,used_h)
        #     dfs(0,minute,0,m,num-i,60,used_m)

        #     for j in h:
        #         for k in m:
        #             res.append(j+':'+ '0'*(len(k)==1) +k)
        # return res
