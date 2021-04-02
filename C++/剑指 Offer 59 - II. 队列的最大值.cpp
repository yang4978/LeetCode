class Solution {
public:
    int trap(vector<int>& height) {
        if(height.size() == 0) {
            return 0;
        }

        int res = 0;
        queue<int> wall;
        wall.push(0);
        int h;
        int l = height.size();
        for(int i=0;i<l;++i) {
            h = height[i];
            if(h >= wall.front()) {
                int edge = min(wall.front(), h);
                wall.pop();
                while(!wall.empty()) {
                    res += edge - wall.front();
                    wall.pop();
                }
            }
            wall.push(h);
        }

        int reverse = l - wall.size();   

        wall = queue<int>();
        wall.push(0);

        for(int i=l-1;i>=reverse;--i) {
            h = height[i];
            if(h >= wall.front()) {
                int edge = min(wall.front(), h);
                wall.pop();
                while(!wall.empty()) {
                    res += edge - wall.front();
                    wall.pop();
                }
            }
            wall.push(h);
        }

        return res;
    }
};
