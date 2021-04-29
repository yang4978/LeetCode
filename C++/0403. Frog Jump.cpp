class Solution {
public:
    bool canCross(vector<int>& stones) {
        set<int> set_stones(stones.begin(), stones.end());
        map<int, set<int>> dp;
        dp[0].insert(0);

        for(auto s:set_stones) {
            for(auto step:dp[s]) {
                for(auto d:{1, 0, -1}) {
                    if((step + d > 0) && set_stones.count(s + step + d)) {
                        dp[s + step + d].insert(step + d);
                    }
                }
            }
        }

        return dp[stones.back()].size() != 0;
    }
};
