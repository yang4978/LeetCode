class Solution {
public:
    int findShortestSubArray(vector<int>& nums) {
        int max_count = 1;
        map<int,vector<int>> num_map;
        for(int i=0;i<nums.size();++i){
            int n = nums[i];
            if(num_map.count(n)!=0){
                max_count = max(max_count, ++num_map[n][0]);
                num_map[n][2] = i;
            }
            else{
                num_map[n] = vector<int>{1,i,i};
            }
        }
        int res  = nums.size();
        for(map<int,vector<int>>::iterator iter = num_map.begin();iter!=num_map.end();++iter){
            if(iter->second[0]==max_count){
                res = min(res,iter->second[2]-iter->second[1]+1);
            }
        }
        return res;
    }
};
