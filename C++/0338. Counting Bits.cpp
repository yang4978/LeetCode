class Solution {
public:
    vector<int> countBits(int num) {
        vector<int> arr={0};
        int bit = 1;
        while((1<<bit)<num){
            bit += 1;
        }
        for(int i=1;i<=bit;++i){
            for(int j=0;j<(1<<(i-1));++j){
                arr.push_back(1+arr[j]);
            }
        }
        if(arr.size()>num){
            arr.assign(arr.begin(),arr.begin()+num+1);
        }
        else{
            arr.push_back(1);
        }
        return arr;
    }
};
