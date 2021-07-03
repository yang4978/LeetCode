class Solution {
public:
    string frequencySort(string s) {
        map<char, int> letter;
        vector<char> arr;
        string res = "";
        for(auto c:s) {
            if(letter.count(c)) {
                letter[c] += 1;
            } else {
                letter[c] = 1;
                arr.push_back(c);
            }
        }
        sort(arr.begin(), arr.end(), [&letter] (char x, char y) {return letter[x] > letter[y];});
        for(auto c:arr) {
            res += string(letter[c], c);
        }
        return res;
    }
};
