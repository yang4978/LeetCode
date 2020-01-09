class Solution:
    def pathSum(self, nums: List[int]) -> int:
        node = [[None]*8 for _ in range(4)]                # 初始化数组

        for n in nums:
            node[n//100-1][(n-n//100*100)//10-1] = n%10    # 将三位整数所携带的节点信息按规则填入数组
                                                        # 百位 n//100 为层数
                                                        # 十位 (n-n//100*100)//10 为所处位置
                                                        # 个位 n%10 为携带值
        #print(*node,sep='\n')                             # 用于检验所得数组是否正确

        res = 0
        
        for i in range(4):                                 # 对数组进行遍历
            for j in range(2**i):                          # 第i层最多包含2^i个节点 
                                    
                if node[i][j] != None and (i==3 or (node[i+1][j*2]==None and node[i+1][j*2+1]==None)):                                                      # 判断是否为叶节点，条件：
                                                        # 1. 节点值非空
                                                        # 2. 节点是否为最底层节点，或者子节点为空
                    res += node[i][j]
                    ii,jj = i,j
                    while ii>0:                            #如果节点为子节点，自下至上回溯直到根节点
                        ii -= 1
                        jj >>= 1
                        res += node[ii][jj]
        
        return res
