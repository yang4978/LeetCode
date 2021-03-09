class Solution {
public:
    string removeDuplicates(string S) {
        string ss;
        for(auto c: S){
            if(!ss.empty() && c==ss.back()){
                ss.pop_back();
            }
            else{
                ss.push_back(c);
            }
        }
        return ss;
    }
};
