class Solution {
public:
    vector<int> decode(vector<int>& encoded) {
        int num0 = 0;
        int num1 = 0;
        int n = encoded.size() + 1;

        for(int i=1;i<=n;++i) {
            num0 ^= i;
        }

        for(int i=1;i<n;i+=2) {
            num1 ^= encoded[i];
        }

        vector<int> arr;

        arr.push_back(num0^num1);

        for(auto x:encoded) {
            arr.push_back(arr.back()^x);
        }

        return arr;

    }
};
