class Solution {
public:
    vector<int> xorQueries(vector<int>& arr, vector<vector<int>>& queries) {
        vector<int> xorArr = {0};
        for(auto x:arr) {
            xorArr.push_back(xorArr.back() ^ x);
        }
        vector<int> res;
        for(auto iter:queries) {
            res.push_back(xorArr[iter[1] + 1] ^ xorArr[iter[0]]);
        }
        return res;
    }
};
