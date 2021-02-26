class Solution {
public:
    vector<int> findNumOfValidWords(vector<string>& words, vector<string>& puzzles) {
        map<int,int> frequency;
        for(auto word:words){
            int mask = 0;
            for(auto c:word){
                mask |= (1<<(c-'a'));
            }
            if(__builtin_popcount(mask)<=7){
                ++frequency[mask];
            }
        }

        vector<int> result;

        for(auto puzzle:puzzles){
            int total = 0;
            for(int choose=0;choose<(1<<6);++choose){
                int mask = 0;
                for(int i=0;i<6;++i){
                    if (choose&(1<<i)){
                        mask |= (1<<(puzzle[i+1]-'a'));
                    }
                }
                mask |= (1<<(puzzle[0]-'a'));
                if(frequency.count(mask)){
                    total += frequency[mask];
                }
            }
            result.push_back(total);
        }
        return result;
    }
};
