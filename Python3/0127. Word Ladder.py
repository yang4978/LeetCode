class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordList = set(wordList)
        start = {beginWord}
        end = {endWord}
        l = len(beginWord)

        if endWord not in wordList:
            return 0
        
        wordList.remove(endWord)

        step = 0

        while start and end:
            step += 1

            if len(start)>len(end):
                start,end = end,start

            temp = set()

            for s in start:
                w = [s[:i]+chr(j)+s[i+1:] for j in range(97,123) for i in range(l)]
                for ws in w:
                    if ws in end:
                        return step + 1
                    if ws in wordList: 
                        wordList.remove(ws)
                        temp.add(ws)

            start = temp
        
        return 0
