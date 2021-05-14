class Solution {
public:
    string intToRoman(int num) {
        vector<int> number ={1,4,5,9,10,40,50,90,100,400,500,900,1000};
        vector<string> letter ={"I","IV","V","IX","X","XL","L","XC","C","CD","D","CM","M"};
        string res;
        int index = letter.size() - 1;
        while(num > 0) {
            if(num >= number[index]) {
                num -= number[index];
                res += letter[index];
            } else {
                index--;
            }
        }
        return res;
    }
};
