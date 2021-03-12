class Solution {
public:
    bool isValidSerialization(string preorder) {
        stack<int> ss;
        ss.push(1);
        int flag = 0;

        for(auto c:preorder){
            if(c==','){
                flag = 0;
                continue;
            }
            
            if(ss.empty()) return false;

            if(c!='#'){
                if(flag == 0){
                    if((--ss.top())==0) ss.pop();
                    ss.push(2);
                    flag = 1;
                }
            }
            else{
                if((--ss.top())==0) ss.pop();
            }
        }
        return ss.empty();
    }
};
