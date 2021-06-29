class Solution {
public:
    string convertToTitle(int columnNumber) {
        string res = "";
        while(columnNumber != 0) {
            int temp = (columnNumber - 1) % 26 + 1;
            res = char(temp - 1 + 'A') +res;
            columnNumber = (columnNumber - temp) / 26;
        }
        return res;
    }
};
