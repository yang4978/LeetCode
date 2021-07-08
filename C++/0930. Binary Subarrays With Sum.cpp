class Solution {
public:
    int numSubarraysWithSum(vector<int>& nums, int goal) {
        unordered_map<int, int> sums;
        int s = 0;
        int res = 0;
        for(auto n:nums) {
            sums[s]++;
            s += n;
            res += sums[s - goal];
        }
        return res;
    }
};
