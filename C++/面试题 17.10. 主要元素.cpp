class Solution {
public:
    int majorityElement(vector<int>& nums) {
        int major;
        int count = 0;

        for(auto n:nums) {
            if(count == 0) {
                major = n;
            }
            count += (major == n) ? 1 : -1;
        }

        count = 0;

        for(auto n:nums) {
            count += (major == n) ? 1 : 0;
        }

        return count > nums.size() / 2 ? major : -1;
    }
};
