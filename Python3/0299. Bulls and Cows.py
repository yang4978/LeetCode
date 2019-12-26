class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        l = len(guess)
        digit_A = collections.defaultdict(int)
        digit_B = collections.defaultdict(int)
        A = 0

        for i in range(l):
            if secret[i] == guess[i]:
                A += 1
            else:
                digit_A[secret[i]] += 1
                digit_B[guess[i]] += 1

        return str(A)+"A"+str(sum(min(digit_A[i],digit_B[i]) for i in digit_A))+"B"
