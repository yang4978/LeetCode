class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:

        def bucket_id(n):
           return n // (t + 1)
        
        bucket = dict()

        for i, n in enumerate(nums):
            if len(bucket) > k :
                del bucket[bucket_id(nums[i - k - 1])]

            bid = bucket_id(n)

            if bucket.get(bid) != None:
                return True
            bucket[bid] = n

            if bucket.get(bid - 1) != None and abs(bucket[bid - 1] - n) <= t:
                return True
            
            if bucket.get(bid + 1) != None and abs(bucket[bid + 1] - n) <= t:
                return True
        
        return False
