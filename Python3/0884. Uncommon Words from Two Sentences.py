class Solution:
    def uncommonFromSentences(self, A: str, B: str) -> List[str]:
        # count = {}
        # for word in A.split():
        #     count[word] = count.get(word, 0) + 1
        # for word in B.split():
        #     count[word] = count.get(word, 0) + 1

        # #Alternatively:
        # #count = collections.Counter(A.split())
        # #count += collections.Counter(B.split())

        # return [word for word in count if count[word] == 1]


        word = {}

        for w in A.split():
            if w not in word:
                word[w] = 1
            else:
                word[w] += 1

        for w in B.split():
            if w not in word:
                word[w] = 1
            else:
                word[w] += 1
        
        return [i for i in word if word[i]==1]
