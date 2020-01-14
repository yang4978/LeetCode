class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if n == 1:                             # 特例，只有一个点时，必然为树
            return True

        if len(edges) != n - 1:                # 对于n个顶点的树而言
            return False                       # 需要满足条件：连通且无环
                                               # 那必然要正好有n-1条边
                                               # 如果边数太少，则有点被孤立
                                               # 如果边数太多，那必然成环

        path = collections.defaultdict(set)    # 利用字典记录连接关系
        for i,j in edges:                      
            path[i] |= {j}
            path[j] |= {i}
        
        if n!=len(path):                       # 如果字典的长度与节点个数不符
            return False                       # 说明字典中缺少某节点
                                               # 也就是说有节点未参与连通图的过程
                                               # 有孤立节点说明不是树
        
        connected = 0                          # 连通域的个数
        for num in range(n):                   # 对n个节点进行遍历
                                               # 如果num在graph中，进行操作
            if num in path:
                queue = {num}                  # 建立队列{num}以便写bfs算法
                                               # 队列保存的是一组连通的点
                while queue:
                    i = queue.pop()            # 从队列中弹出数值i
                    if i in path:              # 如果i在图中
                        queue |= path[i]       # 将与i相连的节点加入队列
                        del path[i]            # 并删除graph[i]
                                               # 防止重复遍历
                
                connected += 1                 # 当该组所有连通的点被遍历结束, 结果+1
                if connected > 1:              # 连通域超过1一个时，不符合树的条件
                    return False               # 返回False

        return True                           
