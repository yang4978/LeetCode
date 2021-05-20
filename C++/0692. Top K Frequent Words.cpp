class Solution {
public:
    vector<string> topKFrequent(vector<string>& words, int k) {
        map<string, int> dict;
        for(auto w:words) {
            dict[w]++;            
        }
        vector<string> arr;

        for(auto x:dict) {
            arr.push_back(x.first);
        }

        sort(arr.begin(), arr.end(), [&dict](string x, string y) {if (dict[x] != dict[y]) return dict[x] > dict[y]; return x < y;});

        arr.erase(arr.begin() + k, arr.end());

        return arr;
    }
};
