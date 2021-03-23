/**
 * // This is the interface that allows for creating nested lists.
 * // You should not implement it, or speculate about its implementation
 * class NestedInteger {
 *   public:
 *     // Return true if this NestedInteger holds a single integer, rather than a nested list.
 *     bool isInteger() const;
 *
 *     // Return the single integer that this NestedInteger holds, if it holds a single integer
 *     // The result is undefined if this NestedInteger holds a nested list
 *     int getInteger() const;
 *
 *     // Return the nested list that this NestedInteger holds, if it holds a nested list
 *     // The result is undefined if this NestedInteger holds a single integer
 *     const vector<NestedInteger> &getList() const;
 * };
 */

class NestedIterator {
private:
    vector<int> arr;
    int index = 0;

public:
    vector<int> dfs(NestedInteger &nest) {
        vector<int> result;
        if(nest.isInteger()) {
            result.push_back(nest.getInteger());
        } else {
            for(auto x:nest.getList()) {
                vector<int> temp = dfs(x);
                result.insert(result.end(), temp.begin(), temp.end());
            }
        }
        return result;
    }

    NestedIterator(vector<NestedInteger> &nestedList) {
        for(auto nest:nestedList) {
            vector<int> temp = dfs(nest);
            arr.insert(arr.end(), temp.begin(), temp.end());
        }
    }
    
    int next() {
        index++;
        return arr[index - 1];
    }
    
    bool hasNext() {
        return index < arr.size();
    }
};

/**
 * Your NestedIterator object will be instantiated and called as such:
 * NestedIterator i(nestedList);
 * while (i.hasNext()) cout << i.next();
 */
