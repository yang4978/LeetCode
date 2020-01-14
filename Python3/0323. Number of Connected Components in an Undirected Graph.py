class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = collections.defaultdict(set)           # 利用字典记录关联信息
        for i,j in edges:                              # 记录关联信息
            graph[i] |= {j}
            graph[j] |= {i}
        
        res = n-len(graph)                             # 由于总共有n个节点
                                                       # 如果graph中有k个节点
                                                       # 那必然有n-k个节点孤立

        for num in range(n):                           # 对n个节点进行遍历
                                                       # 如果num在graph中，进行操作
            if num in graph:
                queue = {num}                          # 建立队列{num}以便写bfs算法
                                                       # 队列保存的是一组连通的点
                while queue:
                    i = queue.pop()                    # 从队列中弹出数值i
                    if i in graph:                     # 如果i在图中
                        queue |= graph[i]              # 将与i相连的节点加入队列
                        del graph[i]                   # 并删除graph[i]
                                                       # 防止重复遍历
                
                res += 1                               # 当该组所有连通的点被遍历结束
                                                       # 结果+1

        return res                                     # 对所有节点进行遍历后，返回res
