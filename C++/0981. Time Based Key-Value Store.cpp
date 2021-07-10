class TimeMap {
    unordered_map<string, vector<string>> kvmap;
    unordered_map<string, vector<int>> ktmap;
public:
    /** Initialize your data structure here. */
    TimeMap() {
    }
    
    void set(string key, string value, int timestamp) {
        kvmap[key].push_back(value);
        ktmap[key].push_back(timestamp);
    }
    
    string get(string key, int timestamp) {
        int l = 0;
        int r = ktmap[key].size();
        int m = -1;

        while(l < r) {
            m = (l + r) >> 1;
            if(ktmap[key][m] <= timestamp) {
                l = m + 1;
            } else {
                r = m;
            }
        }

        if(m == -1 || ktmap[key][m] > timestamp) {
            return "";
        } else {
            return kvmap[key][m];
        }
    }
};

/**
 * Your TimeMap object will be instantiated and called as such:
 * TimeMap* obj = new TimeMap();
 * obj->set(key,value,timestamp);
 * string param_2 = obj->get(key,timestamp);
 */
