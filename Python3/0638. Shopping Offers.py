class Solution:
    def shoppingOffers(self, price: List[int], special: List[List[int]], needs: List[int]) -> int:

        item_num = len(price)

        res = float('inf')

        def shopping(special,needs):
            nonlocal res

            if max(needs) == 0:
                return 0

            special = list(filter(lambda x:all(x[i]<=needs[i] for i in range(item_num)),special))
            
            if not special:
                return sum(price[i]*needs[i] for i in range(item_num))

            return min(p[-1] + shopping(special,[needs[i]-p[i] for i in range(item_num)]) for p in special)
        
        special = list(filter(lambda x: x[-1]<sum(x[i]*price[i] for i in range(item_num)),special))

        return shopping(special,needs)

        # item_num = len(price)

        # res = float('inf')

        # length = len(special)

        # def trackback(needs,index,cost):
        #     nonlocal res

        #     if index == length:
        #         res = min(res,cost+sum(price[i]*needs[i] for i in range(item_num)))
        #         return
            
        #     package = special[index]

        #     max_times = 6

        #     for i in range(item_num):
        #         if package[i]:
        #             if needs[i] == 0:
        #                 max_times = 0
        #                 break
        #             max_times = min(max_times,needs[i]//package[i])
            
        #     for times in range(max_times+1):
        #         new_needs = needs[:]
        #         for i in range(item_num):
        #             new_needs[i] -= times * package[i]

        #         trackback(new_needs,index+1,cost+times*package[-1])
        
        # trackback(needs,0,0)

        # return res
    
