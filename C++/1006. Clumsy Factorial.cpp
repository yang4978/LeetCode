class Solution {
public:
    int clumsy(int N) {
        int result = 0;
        int mod = N % 4;
        int flag = 0;
        int temp = 0;
        for(int i=N;i>0;--i) {
            switch(i % 4 - mod) {
                case 0:
                    temp = i;
                    break;
                case -1:
                case 3:
                    temp *= i;
                    break;
                case -2:
                case 2:
                    temp /= i;
                    break;
                default:
                    if(flag == 0) {
                        result = temp;
                        flag = 1;
                    } else {
                        result += flag * temp;
                        flag = -flag;
                    }
                    result += flag * i;
                    flag = -flag;
                    temp = 0;
                    break;
            }
        }
        if(flag == 0) {
            flag = 1;
        }
        return result + flag * temp;
    }
};
