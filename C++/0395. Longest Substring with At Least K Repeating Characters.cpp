class Solution {
public:
    int longestSubstring(string s, int k) {
        int res = 0;
        for(int t=1;t<=26;++t){
            int l = 0;
            int r = 0;
            vector<int> letter(26,(1<<10));
            int len = 0;
        
            while(r<s.size()){
                
                if((letter[s[r]-'a']) == (1<<10)){
                    len++;
                    letter[s[r]-'a'] = 1;
                }
                else{
                    letter[s[r]-'a']++;
                }

                while(len>t){
                    letter[s[l]-'a'] --;
                    if(letter[s[l]-'a']==0){
                        len--;
                        letter[s[l]-'a'] = (1<<10);
                    }
                    l++;
                }

                if(*min_element(letter.begin(),letter.end())>=k){
                    res = max(res,r-l+1);
                }
                r++;
            }
        }
        return res;
    }
};
