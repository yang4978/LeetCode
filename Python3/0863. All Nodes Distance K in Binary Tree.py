# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distance(self,x0,y0,x1,y1):                  # 根据两个节点的坐标计算距离
        res = 0
                                                     # 如果两个节点不在同一层
                                                     # 首先让layer较大的节点
                                                     # 即较低的节点上移，变成其父节点
                                                     # 对于任意节点，x,y
                                                     # 其父节点坐标为 x-1,y//2
                                                     # 相应地，距离+1
        while x0 > x1:                                
            x0 -= 1
            y0 //= 2
            res += 1
        
        while x0 < x1:
            x1 -= 1
            y1 //= 2
            res += 1
        
        while y0 != y1:                              # 当两节点处于同一层时
                                                     # 需要比较其pos
                                                     # 当pos相等时，两节点即重合
                                                     # 否则两个节点同步上移
                                                     # 由于其layer相等，只需考虑pos
                                                     # 对于任意 pos=y 的节点而言
                                                     # 其父节点pos = y//2
                                                     # 每次上移，距离+2
            y0 //= 2
            y1 //= 2
            res += 2
        
        return res

    def distanceK(self, root: TreeNode, target: TreeNode, K: int) -> List[int]:
        node_val = {}                                # 用于记录节点的坐标和值的对应关系

        queue = [(0,0,root)]                         # 层序遍历的队列，（0,0）为根的坐标
        x,y = 0,0                                    # 记录目标值所对应坐标

        while queue:
            layer,pos,node = queue.pop(0)            # 队列弹出的值分别为层数、位置和节点
            node_val[(layer,pos)] = node.val         # 记录节点的坐标和值的对应关系
                                                     # 即二叉树的坐标化

            if node == target:                       # 找到并记录target对应的节点坐标
                x = layer
                y = pos

            if node.left:                             # 如果节点有左节点
                                                      # 不难想象其坐标值为：
                                                      # layer = layer + 1
                                                      # pos = pos * 2
                queue.append((layer+1,pos*2,node.left))
            
            if node.right:                            # 如果节点有右节点
                                                      # 不难想象其坐标值为：
                                                      # layer = layer + 1
                                                      # pos = pos * 2 + 1
                queue.append((layer+1,pos*2+1,node.right))
                
                                                      # 利用distance函数
                                                      # 计算所有节点与target节点的距离
                                                      # 并返回距离为K的节点值
        return [node_val[p] for p in node_val if self.distance(p[0],p[1],x,y)==K]
