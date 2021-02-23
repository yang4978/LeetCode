class Solution {
public:
    vector<int> getRow(int rowIndex) {
        vector<int> res(rowIndex+1,1);
        for(int i=1;i<=rowIndex;++i){
            res[i] = 1LL*res[i-1]*(rowIndex-i+1)/i;
        }
        return res;
    }
};
