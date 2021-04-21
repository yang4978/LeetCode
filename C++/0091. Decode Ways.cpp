class Solution {
public:
    int numDecodings(string s) {
        int l = s.size();
        vector<int> dp (l + 1, 0);
        dp[l] = 1;
        dp[l - 1] = s[l - 1] != '0' ? 1 : 0;
        for(int i = l - 2; i >= 0; --i) {
            if(s[i] != '0') {
                dp[i] = dp[i + 1];
                if((s[i] - '0') * 10 + s[i + 1] - '0' <= 26) {
                    dp[i] += dp[i + 2];
                }
            }
        }
        return dp[0];
    }
};
