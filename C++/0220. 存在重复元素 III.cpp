class Solution {
public:
    int bucketId(long n, long t) 
    {
        return n < 0 ? -(-n / (t + 1) + 1) : n / (t + 1);
    }

    bool containsNearbyAlmostDuplicate(vector<int>& nums, int k, int t) {        
        map<int, int> bucket;
        long n;
        int id;
        for(int i=0;i<nums.size();++i) {
            n = nums[i]; 

            if(bucket.size() > k) {
                bucket.erase(bucketId(nums[i - k - 1], t));
            }

            id = bucketId(n, t);

            if(bucket.count(id) != 0) {
                return true;
            }

            bucket[id] = n;
            
            if(bucket.count(id - 1) != 0 && abs(n - bucket[id - 1]) <= t ) {
                return true;
            }

            if(bucket.count(id + 1) != 0 && abs(n - bucket[id + 1]) <= t ) {
                return true;
            }
        }
        return false;

    }
};
