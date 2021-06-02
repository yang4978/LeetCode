class Solution {
public:
    bool checkSubarraySum(vector<int>& nums, int k) {
        vector<int> prefix = {0};
        map<int, int> dict;
        for(int i = 0; i < nums.size(); ++i) {
            int n = nums[i];
            int x = prefix.back() + n;
            prefix.push_back(x);
            int mod = x % k;
            if((mod == 0 && i != 0) || (dict.count(mod) && i - dict[mod] > 1)) {
                return true;                
            } else if(dict.count(mod) == 0) {
                dict[mod] = i;
            }
        }
        return false;

    }
};
