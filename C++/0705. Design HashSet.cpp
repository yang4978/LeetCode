class MyHashSet {
private:
    vector<list<int>> data;
    static const int base = 857;
    static int hash(int key){
        return key%base;
    }
public:
    /** Initialize your data structure here. */
    MyHashSet(): data(base) {}
    
    void add(int key) {
        int h = hash(key);
        for(auto i = data[h].begin();i!=data[h].end();i++){
            if((*i)==key) return;
        }
        data[h].push_back(key);
    }
    
    void remove(int key) {
        int h = hash(key);
        for(auto i = data[h].begin();i!=data[h].end();i++){
            if((*i)==key){
                data[h].erase(i);
                return;
            }
        }
    }
    
    /** Returns true if this set contains the specified element */
    bool contains(int key) {
        int h = hash(key);
        for(auto i = data[h].begin();i!=data[h].end();i++){
            if((*i)==key){
                return true;
            }
        }
        return false;
    }
};

/**
 * Your MyHashSet object will be instantiated and called as such:
 * MyHashSet* obj = new MyHashSet();
 * obj->add(key);
 * obj->remove(key);
 * bool param_3 = obj->contains(key);
 */
