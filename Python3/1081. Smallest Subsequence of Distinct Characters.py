class Solution:
    def smallestSubsequence(self, text: str) -> str:
        stack = []
        d = set()
        for i,c in enumerate(text):
            if c not in d:
                while stack!=[] and c<stack[-1] and stack[-1] in text[i+1:]:
                    d.remove(stack.pop())
                stack.append(c)
                d |= {c}
        return ''.join(stack)
