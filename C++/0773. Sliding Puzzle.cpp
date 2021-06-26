class Solution {
public:
    int slidingPuzzle(vector<vector<int>>& board) {
        string start = "";
        int num, temp = 0;
        for(auto arr:board) {
            for(auto c:arr) {
                start += ('0' + c);
                if(c == 0) {
                    num = temp;
                }
                temp++;
            }
        }

        if(start == "123450") {
            return 0;
        }

        queue<tuple<string, int>> q;
        q.push(make_tuple(start, num));

        vector<int> move {-1, 1, -3, 3};
        set<string> used;
        int res = 0;
        string t_start;
        int pos, t_pos;
        while(!q.empty()) {
            int l = q.size();
            res++;
            for(int i = 0; i < l; ++i) {
                start = get<0>(q.front());
                pos = get<1>(q.front());
                q.pop();
                for(auto delta:move) {
                    t_pos = pos + delta;
                    if(t_pos >= 0 && t_pos <= 5 && (t_pos / 3 - pos / 3 == delta / 3)){
                        if(delta > 0) {
                            t_start = start.substr(0, pos) + start[t_pos] + start.substr(pos + 1, t_pos - pos - 1) + start[pos] + start.substr(t_pos + 1, 5 - t_pos);
                        } else {
                            t_start = start.substr(0, t_pos) + start[pos] + start.substr(t_pos + 1, pos - t_pos - 1) + start[t_pos] + start.substr(pos + 1, 5 - pos);
                        }
                        if(t_start == "123450") {
                        return res;
                        }
                        if(used.count(t_start) == 0) {
                            used.insert(t_start);
                            q.push(make_tuple(t_start, t_pos));
                        }
                    }
                }
            }
        }

        return -1;
    }
};
