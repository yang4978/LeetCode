class Solution {
public:
    int openLock(vector<string>& deadends, string target) {
        queue<string> q;
        set<string> s(deadends.begin(), deadends.end());

        if(target == "0000") {
            return 0;
        }

        if(find(deadends.begin(), deadends.end(), "0000") != deadends.end()) {
            return -1;
        }

        q.push("0000");
        int num = 0;
        while(!q.empty()) {
            num++;
            int l = q.size();
            for(int k = 0; k < l; k++) {
                string temp = q.front();
                q.pop();
                for(auto delta:{1, 9}) {
                    for(int i = 0; i < 4; ++i) {
                        string tt = temp.substr(0, i) + char((temp[i] - '0' + delta) % 10 + '0') + temp.substr(i + 1, 4 - i -1);
                        if(tt == target) {
                            return num;
                        }
                        if(s.count(tt) == 0) {
                            q.push(tt);
                            s.insert(tt);
                        }
                    }
                }
            }
        }
        return -1;
    }
};
