class Solution:
    def removeDuplicates(self, S: str) -> str:
        # while(re.search(r'([a-z])\1',S)):
        #     S = re.sub(r'([a-z])\1','',S)
        # return S
        stack = []
        for i in S:
            if stack!=[] and i == stack[-1]:
                stack.pop()
            else:
                stack.append(i)
        return ''.join(stack)
