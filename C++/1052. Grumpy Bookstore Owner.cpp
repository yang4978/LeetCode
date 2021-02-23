class Solution {
public:
    int maxSatisfied(vector<int>& customers, vector<int>& grumpy, int X) {
        int len = customers.size();
        int temp = 0;
        for(int i=0;i<len;++i){
            temp += grumpy[i]==0?customers[i]:0;
        }
        for(int i=0;i<X;++i){
            temp += grumpy[i]==1?customers[i]:0;
        }

        int res = temp;
        int l = 0;
        int r = X;

        while(r<len){
            temp -= grumpy[l++]==1?customers[l-1]:0;
            temp += grumpy[r++]==1?customers[r-1]:0;
            res = max(res,temp);
        }
        return res;
    }
};
