class Solution {
public:
    int combinationSum4(vector<int>& nums, int target) {
        sort(nums.begin(), nums.end());
        vector<int> dp (target + 1, 0);
        dp[0] = 1;
        for(int i = 1; i <= target; ++i) {
            for(auto n : nums) {
                if(i >= n && dp[i - n] < INT_MAX - dp[i]) {
                    dp[i] += dp[i - n];
                }
            }
        }
        return dp.back();
    }
};
