class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        person = sorted(people, key=lambda x: (-x[0],x[1]))
        res = []
        for pair in person:
            res.insert(pair[1],pair)
        return res

        # height = set();
        # height_block = collections.defaultdict(list);
        # queue = [];
        # order = collections.defaultdict(int)

        # for pair in people:
        #     h,k = pair
        #     height.add(h)
        #     height_block[h].append(pair)
        #     order[h] = 0
        
        # height = sorted(list(height))

        # for h in height:
        #     height_block[h].sort(key=lambda x:-x[1])
        
        # print(height_block)
        
        # while len(queue)<len(people): 
        #     last_num = -1
        #     for i in range(len(height)):
        #         h = height[i]
        #         num = order[h]
        #         if num<=last_num:
        #             break

        #         if height_block[h]!=[] and height_block[h][-1][1] == num:
        #             queue.append(height_block[h].pop())
        #             last_num = num
        #             for j in range(i+1):
        #                 order[height[j]] += 1
            
        # return queue
