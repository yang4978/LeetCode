class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        # if not answers:
        #     return 0
        
        # rabbit = collections.defaultdict(int)

        # for i in answers:
        #     rabbit[i] += 1
        
        # return sum(math.ceil(rabbit[i]/(i+1))*(i+1) for i in rabbit)

        return sum(math.ceil(answers.count(i)/(i+1))*(i+1) for i in set(answers)) if answers else 0
