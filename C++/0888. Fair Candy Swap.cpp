// class Solution {
// public:
//     vector<int> fairCandySwap(vector<int>& A, vector<int>& B) {
//         int diff = (accumulate(A.begin(),A.end(),0) - accumulate(B.begin(),B.end(),0))/2;
//         for(int i=0;i<A.size();i++){
//             vector<int>::iterator iter = find(B.begin(),B.end(),A[i] - diff);
//             if (B.end()!=iter){
//                 vector<int> result(2);
//                 result[0] = A[i];
//                 result[1] = B[iter-B.begin()];
//                 return result;
//             }
//         }
//     }
// };

// class Solution {
// public:
//     vector<int> fairCandySwap(vector<int>& A, vector<int>& B) {
//         int diff = (accumulate(A.begin(),A.end(),0) - accumulate(B.begin(),B.end(),0))/2;
//         set<int> A_set(A.begin(),A.end());
//         set<int> B_set(B.begin(),B.end());
//         for(set<int>::iterator i=A_set.begin();i!=A_set.end();i++){
//             if (B_set.find(*i- diff)!=B_set.end()){
//                 vector<int> result(2);
//                 result[0] = *i;
//                 result[1] = *i - diff;
//                 return result;
//             }
//         }
//     }
// };

// class Solution {
// public:
//     vector<int> fairCandySwap(vector<int>& A, vector<int>& B) {
//         int diff = (accumulate(A.begin(),A.end(),0) - accumulate(B.begin(),B.end(),0))/2;
//         unordered_set<int> rec(A.begin(),A.end());
//         vector<int> ans;
//         for(auto& value:B){
//             if (rec.count(value+diff)){
//                 ans = vector<int>{value+diff,value};
//                 break;
//             }
//         }
//         return ans;
//     }
// };

class Solution {
public:
    vector<int> fairCandySwap(vector<int>& A, vector<int>& B) {
        int diff = (accumulate(A.begin(),A.end(),0) - accumulate(B.begin(),B.end(),0))/2;
        int l,r;
        vector<int> ans;
        sort(B.begin(),B.end());
        for(auto& a:A){
            l = 0;
            r = B.size()-1;
            int b = a - diff;
            while (l < r){
                int mid = (l+r)/2;
                if (B[mid] >= b){
                    r = mid;
                }
                else{
                    l = mid + 1;
                }
            }
            if (B[l] == b){
                ans = vector<int>{a,b};
                break;
            }
        }
        return ans;
    }
};
