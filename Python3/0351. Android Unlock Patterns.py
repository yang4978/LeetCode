class Solution:
    def numberOfPatterns(self, m: int, n: int) -> int:
        '''
        dfs算法，带入的参数分别为：
        index: 上一次滑动经过的数字
        used: 数字的使用情况，由于题目于要求点不能重复，所以如果数字被使用过，则略过该情况
        limit: 保存数字滑动限制条件的列表
        num: 已经滑动的数字个数
        res: 计算结果
        m,n: 题目中提供的上下界

        dfs算法的一般流程为：
        1. 设置返回/终止条件，本题中终止条件为数字个数超过上界
        2. 考虑返回值，题目中的返回值为res
        3. 进行循环遍历，值得注意的是，每次遍历结束后，都应将条件初始化，防止影响下一次计算
        '''


        def dfs(index,used,limit,num,res,m,n):
            '''
            1. 设置终止条件：当num超过上界时，返回res值
            '''
            if num>n:
                return res

            '''
            2. 考虑当计算过程中的返回值，num在[m,n]之间时，res+1
            '''
            if m<=num<=n:
                res += 1

            '''
            3. 开始循环遍历，每次从[1,9]中选择一个数值作为下一步要经过的数字i，
            当这个数值未被使用过，且上一步经过的数字index与i之间需要经过的数字
            已经被使用过时，才进行循环。
            '''
            for i in range(1,10):
                if used[i] == False and used[limit[index][i]]==True:

                    # i被使用了，所以标记为使用过的数字
                    # 经过的数字数num也要相应+1
                    used[i] = True
                    num += 1

                    #开始循环
                    res = dfs(i,used,limit,num,res,m,n)

                    # 初始化条件，即i未被使用过
                    # 同时经过的数字数为原来的num
                    used[i] = False
                    num -= 1
            return res

        '''
        为了建立保存数字滑动限制条件的列表limit，首先要考虑每个数字在手机键盘中的位置
        '''    
        pos={}
        for i in range(1,10):
            pos[i] = [(i-1)//3,i-1-(i-1)//3*3]

        '''
        计算limit列表
        为了使数字与行列数一致，这里建立了一个10*10的列表，初始值为0
        列表中任意值limit[i][j]的含义为从数字i到j需要经过limit[i][j]
        如果limit[i][j]=0，说明两个数值可以直接到达
        也就是说默认used[0]=True
        '''
        limit = [[0]*10 for i in range(10)]

        for i in range(1,10):
            for j in range(i+1,10):
                x_i,y_i = pos[i]
                x_j,y_j = pos[j]
                
                #判断条件：九宫格中，两个数字的行数和列数至少有一个相差值为2，同时两数之和为偶数
                if (abs(x_i-x_j)==2 or abs(y_i-y_j)==2) and (i+j)%2==0:
                    limit[i][j] = (i+j)//2
                    limit[j][i] = (i+j)//2

        #所有值的初始化
        index = 0
        used = [True]+[False]*9
        num = 0
        res = 0
        res = dfs(0,used,limit,num,res,m,n)

        return res
