class Solution {
public:
    string reverseParentheses(string s) {
        vector<char> ss;
        for(auto c:s) {
            if(c != ')') {
                ss.push_back(c);
            } else {
                char t = ss.back();
                ss.pop_back();
                vector<char> temp;
                while(t != '(') {
                    temp.push_back(t);
                    t = ss.back();
                    ss.pop_back();
                }
                ss.insert(ss.end(), temp.begin(), temp.end());
            }
        }
        string res;
        for(auto c:ss) {
            res += c;
        }
        return res;
    }
};
