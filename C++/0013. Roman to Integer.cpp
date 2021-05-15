class Solution {
public:
    int romanToInt(string s) {
        map<char, int> num = {{'I',1}, {'V',5}, {'X',10}, {'L',50}, {'C',100}, {'D',500}, {'M',1000}};
        int res = 0;
        int temp = 0;
        for(char c:s) {
            if(temp < num[c]) {
                res -= temp;
            } else {
                res += temp;
            }
            temp = num[c];
        }
        return res + temp;
    }
};
