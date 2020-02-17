class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        def dfs(row,arr):                   # 回溯的主体
                                            # row为当前考虑的行数
                                            # pos为表明无法放置位置的矩阵
                                            # arr是每一行Q所在的列数

            if row == n:                    # 行数row为n时，说明已经找到填写的位置
                                            # 在表示结果的res数组中填写结果
                res.append(['.'*i + 'Q' + '.'*(n-1-i) for i in arr])
                return                      # 返回

            for col in range(n):            # 对于可能的列col
                flag = 0                    # 设置flag

                for t_row in range(row):    # 调用先前每一个皇后的位置
                                            # 其中t_row是行数，arr[t_row]是列数

                                            # 如果当前列数与先前皇后列数相等
                                            # 或者列数差的绝对值和行数差相等（对角线）
                                            # 则将flag置为1，并break
                    if col == arr[t_row] or row-t_row == abs(col-arr[t_row]):
                        flag = 1
                        break
                if flag == 0:               # 如果flag为0，说明该位置可放置王后
                                            # 继续计算下一行
                    dfs(row+1,arr+[col])

        res = []                             # 初始化参数
        row = 0
        arr = []
                                             # 初始调用dfs函数
        dfs(row,arr)
        return res
        
        # def arrange(t,row,col):           # 对于第row行第col列放置的棋子
        #                                     # 计算因为它而无法放置的位置
        #                                     # 并记录在数组t中
        #                                     # 由于dfs算法逐行放置棋子
        #                                     # 这里不需要考虑同一行的情况

        #     for i in range(row,n):          # 同一列无法放置的位置
        #                                     # 由于dfs算法逐行放置
        #                                     # 因此小于row行的位置不予考虑
        #         t[i][col] = 1


        #     directions = [(1,1),(1,-1)]    # 计算对角线和反对角线无法放置的位置
        #                                     # 同样不考虑小于row行的位置
        #                                     # 即dx都为1

        #     for dx,dy in directions:
        #         x = row
        #         y = col
        #         while x+dx<n and 0<=y+dy<n: # 由于dx都为1
        #                                     # 这里不需要考虑x+dx<0的边界条件
        #             t[x+dx][y+dy] = 1
        #             x += dx
        #             y += dy
        #     return t


        # def dfs(row,pos,arr):            # 回溯的主体
        #                                     # row为当前考虑的行数
        #                                     # pos为表明无法放置位置的矩阵
        #                                     # arr是每一行Q所在的列数

        #     if row == n:                    # 行数row为n时，说明已经找到填写的位置
        #                                     # 在表示结果的res数组中填写结果
        #         res.append(['.'*i + 'Q' + '.'*(n-1-i) for i in arr])
        #         return                      # 返回

        #     for col in range(n):            
        #         if pos[row][col] == 0:      # 查找当前行可放置棋子的列数
        #                                     # 计算在放置该棋子情况下的pos矩阵，即temp

        #                                     # 为了放置pos矩阵在调用函数过程中被更改
        #                                     # 需要逐行复制原来的pos矩阵
        #             temp = arrange([pos_row[:] for pos_row in pos],row,col)
        #                                     # 继续对下一行进行计算
        #             dfs(row+1,temp,arr+[col])


        # res = []                             # 初始化参数
        # row = 0
        # pos = [[0]*n for _ in range(n)]
        # arr = []
        #                                      # 初始调用dfs函数
        # dfs(row,pos,arr)
        # return res
