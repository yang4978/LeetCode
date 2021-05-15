/*
// Definition for Employee.
class Employee {
public:
    int id;
    int importance;
    vector<int> subordinates;
};
*/

class Solution {
public:
    int getImportance(vector<Employee*> employees, int id) {
        map<int, int> emp_import;
        map<int, vector<int>> emp_sub;
        queue<int> q;
        q.push(id);

        for(auto e:employees) {
            emp_import[e->id] = e->importance;
            emp_sub[e->id] = e->subordinates;
        }

        int res = 0;

        while(!q.empty()) {
            int num = q.front();
            q.pop();
            res += emp_import[num];
            for(auto i:emp_sub[num]) {
                q.push(i);
            }
        }
        return res;
    }
};
