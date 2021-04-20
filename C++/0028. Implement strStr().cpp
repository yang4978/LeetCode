class Solution {
public:
    int strStr(string haystack, string needle) {
        int l = needle.size();

        if(haystack.size() < l) {
            return -1;
        }

        if(l == 0) {
            return 0;
        }

        for(int i=0;i<=haystack.size()-l;++i) {
            if(haystack[i] == needle[0] && haystack.substr(i, l) == needle) {
                return i;
            }
        }

        return -1;

    }
};
