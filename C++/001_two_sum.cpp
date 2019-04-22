//https://leetcode.com/problems/two-sum/submissions/

class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int, int> mp;
        for(int i=0;i<nums.size();i++){
            if(mp.find(nums[i])!=mp.end()){
                int x = mp[nums[i]];
                return{mp[nums[i]],i};
            }
            else{
                mp[target-nums[i]] = i;
            }
        }
        //without this return, a warning called "control reaches end of non-void function" will be regarded as error
        //this error means that maybe the function has no return value even when we finish the loop
        return {0,0};
    }
};
