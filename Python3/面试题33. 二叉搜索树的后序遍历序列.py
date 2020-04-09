class Solution:
    def verifyPostorder(self, postorder: List[int]) -> bool:
        if len(postorder) <= 1:
            return True

        inorder = sorted(postorder)
        num = postorder.pop()
        i = inorder.index(num)

        left = postorder[:i]
        right = postorder[i:]

        if (left and max(left) > num) or (right and min(right) < num):
            return False

        return self.verifyPostorder(left) and self.verifyPostorder(right)
