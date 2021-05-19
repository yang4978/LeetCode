class Solution {
public:
    int kthLargestValue(vector<vector<int>>& matrix, int k) {
        int m = matrix.size();
        int n = matrix[0].size();

        vector<int> res;
        vector<vector<int>> arr (m, vector<int>(n, 0));

        arr[0][0] = matrix[0][0];
        res.push_back(arr[0][0]);

        int t;

        for(int i = 1; i < m; ++i) {
            t = arr[i - 1][0] ^ matrix[i][0];
            arr[i][0] = t;
            res.push_back(t);
        }

        for(int j = 1; j < n; ++j) {
            t = arr[0][j - 1] ^ matrix[0][j];
            arr[0][j] = t;
            res.push_back(t);
        }

        for(int i = 1; i < m; ++i) {
            for(int j = 1; j < n; ++j) {
                t = matrix[i][j] ^ arr[i - 1][j] ^ arr[i][j - 1] ^arr[i - 1][j - 1];
                arr[i][j] = t;
                res.push_back(t);
            }
        }

        sort(res.rbegin(), res.rend());
        return res[k - 1];

    }
};
