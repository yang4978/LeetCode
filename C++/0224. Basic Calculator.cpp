class Solution {
public:
    long long calculate(string s) {
        string ss;
        long long res = 0;
        long long temp = 0;
        long long power = 1;
        char x;

        for(auto c:s){
            if(c==' ') continue;
            else if(c==')'){
                x = ss.back();
                ss.pop_back();
                while(x!='('){
                    switch(x){
                        case '+':
                            res += temp;
                            temp = 0;
                            power = 1;
                            break;
                        case '-':
                            res -= temp;
                            temp = 0;
                            power = 1;
                            break;
                        default:
                            temp += (x-'0')*power;
                            power *= 10;
                            break;
                    }
                    x = ss.back();
                    ss.pop_back();
                }
                res += temp;
                temp = 0;
                power = 1;

                if(!ss.empty() && ss.back()!='-' && ss.back()!='+'){
                    ss.push_back('+');
                }

                if(!ss.empty() && res<0 and ss.back()=='-'){
                    ss.pop_back();
                    ss.push_back('+');
                    res = -res;
                }
                
                for(auto x:to_string(res)){
                    ss.push_back(x);
                }
                res = 0;
            }
            else ss.push_back(c);
        }

        while(!ss.empty()){
            x = ss.back();
            ss.pop_back();
            switch(x){
                case '+':
                    res += temp;
                    temp = 0;
                    power = 1;
                    break;
                case '-':
                    res -= temp;
                    temp = 0;
                    power = 1;
                    break;
                default:
                    temp += (x-'0')*power;
                    power *= 10;
                    break;
                    }
        }
        res += temp;
        return res;
    }
};
