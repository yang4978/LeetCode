class Solution {
public:
    /*bool cmp(int x, int y, const vector<vector<int>>& mat) {
        int sx = accumulate(mat[x].begin(), mat[x].end(), 0);
        int sy = accumulate(mat[y].begin(), mat[y].end(), 0);
        if(sx != sy) {
            return sx < sy;
        } else {
            return x < y;
        }
    }
    vector<int> kWeakestRows(vector<vector<int>>& mat, int k) {
        int l = mat.size();
        vector<int> arr;
        for(int i=0;i<l;++i) {
            arr.push_back(i);
        }
        sort(arr.begin(), arr.end(), [this, mat](int x, int y){ return cmp(x, y, mat); });
        return vector<int>(arr.begin(), arr.begin() + k);
    }*/

    vector<int> kWeakestRows(vector<vector<int>>& mat, int k) {
        int l = mat.size();
        vector<int> arr;
        vector<int> total;
        for(int i=0;i<l;++i) {
            arr.push_back(i);
            total.push_back(accumulate(mat[i].begin(), mat[i].end(), 0));
        }
        sort(arr.begin(), arr.end(), [total](int x, int y){ if(total[x] != total[y])return total[x] < total[y]; return x < y; });
        return vector<int>(arr.begin(), arr.begin() + k);
    }
};
