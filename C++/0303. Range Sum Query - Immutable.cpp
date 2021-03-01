#include<vector>
class NumArray {
public:
    vector<int> sums={0};
    NumArray(vector<int>& nums) {
        for(auto n:nums){
            sums.push_back(sums.back()+n);
        }
    }
    
    int sumRange(int i, int j) {
        return sums[j+1] - sums[i];
    }
};

/**
 * Your NumArray object will be instantiated and called as such:
 * NumArray* obj = new NumArray(nums);
 * int param_1 = obj->sumRange(i,j);
 */
