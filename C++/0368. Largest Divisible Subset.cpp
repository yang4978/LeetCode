class Solution {
public:
    vector<int> largestDivisibleSubset(vector<int>& nums) {
        sort(nums.begin(), nums.end());
        int l = nums.size();
        vector<int> dp(l, 1);
        for(int i = 0; i < l; ++i) {
            for(int j = i - 1; j >= 0; --j) {
                if(nums[i] % nums[j] == 0) {
                    dp[i] = max(dp[i], dp[j] + 1);
                }
            }
        }

        int target = *max_element(dp.begin(), dp.end());
        int i = l - 1;
        vector<int> res(target, 0);
        while(target > 0) {
            if(dp[i] == target && (res.back() == 0 || res[target] % nums[i] == 0)) {
                target--;
                res[target] = nums[i];
            }
            i--;
        }
        return res;
    }
};
