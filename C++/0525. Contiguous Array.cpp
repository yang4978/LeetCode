class Solution {
public:
    int findMaxLength(vector<int>& nums) {
        int c = 0;
        int res = 0;
        map<int, int> digit;
        digit[0] = -1;
        for(int i = 0; i < nums.size(); i++) {
            if(nums[i] == 0) {
                c--;
            } else {
                c++;
            }
            if(digit.count(c)) {
                res = max(res, i - digit[c]);
            } else {
                digit[c] = i;
            }
        }
        return res;
    }
};
