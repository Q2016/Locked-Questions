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











We should not use advanced data structures, remove from deque has an O(n) time complexity

Solution: Double-Linked list

https://www.youtube.com/watch?v=7ABFKPK2hD4    
    
    
class Node:
    def __init__(self, key, val):
        self.key, self.val= key, val
        self.prev = self.next=None
        
        
class LRUCashe:
    def __init__(self, capacity):
        self.cap=capacity
        self.cashe={} # map key to node
        
        # left=LRU, right=most recent
        self.left, self.right= Node(0, 0), Node(0, 0)
        self.left.next, self.right.prev= self.right, self.left
        
    # remove node from list
    def remove(self, node):
        prev, nxt= node.prev, node.next
        prev.next, nxt.prev=nxt, prev
        
    # insert node at right
    def insert(self, node):
        prev, nxt=self.right.prev, self.right
        prev.next=nxt.prev=node
        
    def get(self, key):
        if key in self.cashe:
            self.remove(self.cash[key])
            self.inserst(self.cashe[key])
            return self.cashe[key].val
        return -1
    
    def put(self, key, value):
        if key in self.cashe:
            self.remove(self.cashe[key])
        self.cashe[key]=Node(key, value)
        self.insert(self.cashe[key])
        
        if len(self.cashe) > self.cap:
            # remove from the list and delete the LRU from the hashmap
            lru= self.left.next
            self.remove(lru)
            del self.cashe[lru.key]
            
   
