class Solution:
    arr = set()                            # 全局变量，集合arr

    def calculateSum(self,root):           # 计算每一层的sum值
        if not root:                       # 非节点，返回0
            return 0
                                           # 计算该节点值与左子树和右子树对应sum的总和
        res = root.val + self.calculateSum(root.left) + self.calculateSum(root.right)
        
        self.arr.add(res)                  # 将sum加入集合

        return res                         # 返回sum

    def maxProduct(self, root: TreeNode) -> int:
        self.arr = set()                   # 初始化arr
        node_sum = self.calculateSum(root) # 计算总和
        res = 0

        for i in self.arr:
            res = max(res,i*(node_sum-i))  # 对集合arr中的值进行遍历
                                           # 由于arr中的值为每个子树的总和
                                           # sum - 子树总和即为剩余部分的总和
                                           # 两者相乘即为分裂二叉树的乘积
                                           # 获取最大的乘积结果即可

        res %= (10**9+7)                   # 求模

        return res
