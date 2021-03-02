class NumMatrix {
public:
    vector<vector<int>> arr;
    NumMatrix(vector<vector<int>>& matrix) {
        int m = matrix.size();

        if(m==0){
            return;
        }

        int n = matrix[0].size();

        arr = vector<vector<int>>(m,vector<int>(n,0));

        for(int i=0;i<m;++i){
            for(int j=0;j<n;++j){
                arr[i][j] = matrix[i][j];
            }
        }

        for(int i=1;i<m;++i){
            for(int j=0;j<n;++j){
                arr[i][j] += arr[i-1][j];
            }
        }

        for(int i=0;i<m;++i){
            for(int j=1;j<n;++j){
                arr[i][j] += arr[i][j-1];
            }
        }

    }
    
    int sumRegion(int row1, int col1, int row2, int col2) {
        int res = arr[row2][col2];

        if(row1>0){
            res -= arr[row1-1][col2];
        }

        if(col1>0){
            res -= arr[row2][col1-1];
        }

        if(row1>0&&col1>0){
            res += arr[row1-1][col1-1];
        }
        return res;
    }
};

/**
 * Your NumMatrix object will be instantiated and called as such:
 * NumMatrix* obj = new NumMatrix(matrix);
 * int param_1 = obj->sumRegion(row1,col1,row2,col2);
 */
