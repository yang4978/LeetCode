class Solution {
public:
    bool canShip(vector<int>& weights, int D, int cap) {
        int day = 1;
        int init = 0;
        for(auto w:weights) {
            if(init + w > cap) {
                init = w;
                day++;
                if(day > D) {
                    return false;
                }
            } else {
                init += w;
            }
        }
        return true;
    }
    int shipWithinDays(vector<int>& weights, int D) {
        int left = *max_element(weights.begin(), weights.end());
        int right = accumulate(weights.begin(), weights.end(), 0);
        while(left < right) {
            int mid = (left + right) >> 1;
            if(canShip(weights, D, mid)) {
                right = mid;
            } else {
                left = mid + 1;
            }
        }
        return left;
    }
};
