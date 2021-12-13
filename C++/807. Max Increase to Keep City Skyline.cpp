class Solution {
public:
    int maxIncreaseKeepingSkyline(vector<vector<int>>& grid) {
        int n = grid.size();
        int res = 0;
        vector<int> xmax(n, 0);
        vector<int> ymax(n, 0);
        for(int i=0;i<n;i++) {
            xmax[i] = *max_element(grid[i].begin(), grid[i].end());
        }
        for(int j=0;j<n;j++) {
            for(int i=0;i<n;i++) {
                ymax[j] = max(ymax[j], grid[i][j]);
            }
            for(int i=0;i<n;i++) {
                res += min(xmax[i], ymax[j]) - grid[i][j];
            }
        }
        return res;
    }
};
