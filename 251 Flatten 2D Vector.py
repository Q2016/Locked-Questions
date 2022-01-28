Question:
Implement an iterator to flatten a 2d vector.

Example, Given 2d vector =[[1,2],[3],[4,5,6]]. By calling next repeatedly until hasNext returns false, the order of elements 
returned by next should be: [1,2,3,4,5,6].


Solution:
  
class Vector2D:
    x, y = 0, 0
    vec = None

    # Initialize your data structure here.
    # @param {integer[][]} vec2d
    def __init__(self, vec2d):
        self.vec = vec2d
        self.x = 0
        if self.x != len(self.vec):
            self.y = 0
            self.adjustNextIter()

    # @return {integer}
    def next(self):
        ret = self.vec[self.x][self.y]
        self.y += 1
        self.adjustNextIter()
        return ret

    # @return {boolean}
    def hasNext(self):
        return self.x != len(self.vec) and self.y != len(self.vec[self.x])

    def adjustNextIter(self):
        while self.x != len(self.vec) and self.y == len(self.vec[self.x]): 
            self.x += 1
            if self.x != len(self.vec):
                self.y = 0

# Time:  O(1)
# Space: O(1)                
