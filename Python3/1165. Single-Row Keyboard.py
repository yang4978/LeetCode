    def calculateTime(self, keyboard: str, word: str) -> int:
        letter ={}
        for i in range(26):
            letter[keyboard[i]] = i
        # position = [0]
        # for i in word:
        #     position.append(letter[i])
        # return sum(abs(position[i]-position[i-1]) for i in range (1,len(position)))
        before = 0
        result = 0
        for i in word:
            result += abs(letter[i]-before)
            before = letter[i]
            
        return result
