class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:      

        if endWord not in wordList:
            return []

        min_len = 0
        res = []
        l = len(beginWord)

        wordList = set(wordList)
        word_combo = collections.defaultdict(list)

        for w in wordList:
            for i in range(l):
                word_combo[w[:i]+'*'+w[i+1:]].append(w)
        
        visited = dict()

        queue = [(beginWord,[beginWord],1)]

        while queue:
            word, path, length = queue.pop(0)
            for i in range(l):
                temp_word = word[:i]+'*'+word[i+1:]
                for s in word_combo[temp_word]:
                    if s==endWord:
                        if min_len==0 or length+1<min_len:
                            res = [path+[s]]
                            min_len = length+1
                        elif length+1==min_len:
                            res.append(path+[s])
                    
                    if s not in visited or visited[s]>=length+1:
                        visited[s] = length + 1
                        queue.append((s,path+[s],length+1))

        return res
