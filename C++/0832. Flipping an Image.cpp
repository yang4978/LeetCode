class Solution {
public:
    vector<vector<int>> flipAndInvertImage(vector<vector<int>>& A) {
        vector<vector<int>> res;
        for(auto arr:A){
            vector<int> temp;
            for(vector<int>::iterator iter = arr.end()-1;iter>=arr.begin();iter--){
                temp.push_back(1^(*iter));
            }
            res.push_back(temp);
        }
        return res;
    }
};
