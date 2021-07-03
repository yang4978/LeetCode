class Solution {
public:
    int numWays(int n, vector<vector<int>>& relation, int k) {
        map<int, vector<int>> num;
        map<int, int> res;
        res[0] = 1;

        for(auto arr:relation) {
            num[arr[0]].push_back(arr[1]);
        }

        for(int i = 0; i < k; ++i) {
            map<int, int> temp;
            for(auto iter:res) {
                for(auto j:num[iter.first]){
                    if(temp.count(j) == 0) {
                        temp[j] = res[iter.first];
                    } else {
                        temp[j] += res[iter.first];
                    }
                }
            }
            res = temp;
        }

        return res[n - 1];
    }
};
