Question:
Design and implement a data structure for Least Recently Used (LRU) cache.
It should support the following operations: get and put.
get(key) - Get the value (will always be positive) of the key if the key exists in the cache, otherwise return -1.
put(key, value) - Set or insert the value if the key is not already present.
When the cache reached its capacity, it should invalidate the least recently used item before inserting a new item.
Follow up: Could you do both operations in O(1) time complexity?

Example:
LRUCache cache = new LRUCache( 2 /* capacity */ );
cache.put(1, 1);
cache.put(2, 2);
cache.get(1);       // returns 1
cache.put(3, 3);    // evicts key 2
cache.get(2);       // returns -1 (not found)
cache.put(4, 4);    // evicts key 1
cache.get(1);       // returns -1 (not found)
cache.get(3);       // returns 3    




Solution:

def __init__(self, capacity):
    self.dic = collections.OrderedDict()
    self.remain = capacity

def get(self, key):
    if key not in self.dic:
        return -1
    v = self.dic.pop(key) 
    self.dic[key] = v   # set key as the newest one
    return v

def set(self, key, value):
    if key in self.dic:    
        self.dic.pop(key)
    else:
        if self.remain > 0:
            self.remain -= 1  
        else:  # self.dic is full
            self.dic.popitem(last=False) 
    self.dic[key] = value
        
        
C++:
class LRUCache {
private:
    int capacity;
    list<int> recent;
    unordered_map<int, int> cache;
    unordered_map<int, list<int>::iterator> pos;
    void use(int key) {
        if (pos.find(key) != pos.end()) {
            recent.erase(pos[key]);
        } else if (recent.size() >= capacity) {
            int old = recent.back();
            recent.pop_back();
            cache.erase(old);
            pos.erase(old);
        }
        recent.push_front(key);
        pos[key] = recent.begin();
    }
public:
    LRUCache(int capacity): capacity(capacity) {}
    int get(int key) {
        if (cache.find(key) != cache.end()) {
            use(key);
            return cache[key];
        }
        return -1;
    }
    void set(int key, int value) {
        use(key);
        cache[key] = value;
    }
};   
