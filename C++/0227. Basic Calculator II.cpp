class Solution {
public:
    int calculate(string s) {
        vector<int> ss;
        s.push_back('+');
        char presign = '+';
        int temp = 0;

        for(auto c:s){
            if(c == ' ') continue;
            else if(isdigit(c)){
                temp = 10*temp + (c-'0');
            }
            else{
                switch(presign){
                    case '+':
                        ss.push_back(temp);
                        break;
                    case '-':
                        ss.push_back(-temp);
                        break;
                    case '*':
                        ss.back() *= temp;
                        break;
                    default:
                        ss.back() /= temp;
                        break;
                }   
                presign = c;
                temp = 0;
            }
        }
        return accumulate(ss.begin(),ss.end(),0);
    }
};
