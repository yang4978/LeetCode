class Solution {
public:
    int countPairs(vector<int>& deliciousness) {
        unordered_map<int, int> meals;
        int max_num = *(max_element(deliciousness.begin(), deliciousness.end())) * 2;
        int res = 0;
        int mod = pow(10, 9) + 7;
        for(auto d:deliciousness) {
            int exp = 1;
            while(exp <= max_num) {
                if(meals.count(exp - d)) {
                    res = (res + meals[exp - d]) % mod;
                }
                exp <<= 1;
            }
            meals[d]++;
        }
        return res;
    }
};
