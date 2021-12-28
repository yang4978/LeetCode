class Solution {
public:
    int maxLengthBetweenEqualCharacters(string s) {
        int res = -1;
        map<char, int> letter_min;
        for(int i = 0; i < s.size(); ++i) {
            if(letter_min.count(s[i]) == 0) {
                letter_min[s[i]] = i;
            } else {
                res = max(res, i - letter_min[s[i]] - 1);
            }
        }
        return res;
    }
};
