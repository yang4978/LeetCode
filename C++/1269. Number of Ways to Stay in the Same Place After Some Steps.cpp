class Solution {
public:
    int numWays(int steps, int arrLen) {
        int l = min(steps / 2 + 1, arrLen);
        vector<vector<int>> arr (2, vector<int>(l, 0));
        int before = 0;
        int after;
        arr[before][0] = 1;
        const int mod = pow(10, 9) + 7;
        
        for(int s = 1; s <= steps; ++s) {
            after = 1 - before;
            for(int i = 0; i < l; ++i) {
                arr[after][i] = arr[before][i];
                if(i - 1 >= 0) {
                    arr[after][i] += arr[before][i - 1];
                    arr[after][i] %=  mod;
                }
                if(i + 1 < l) {
                    arr[after][i] += arr[before][i + 1];
                    arr[after][i] %=  mod;
                }   
            }
            before = after;
        }
        
        return arr[after][0];
    }
};
