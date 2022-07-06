Question:
Given two 1d vectors, implement an iterator to return their elements alternately. For example, given two 1d vectors:
v1 = [1, 2], v2 = [3, 4, 5, 6]
By calling next repeatedly until hasNext returns false, the order of elements returned by next should be: [1, 3, 2, 4, 5, 6].
Follow up: What if you are given k 1d vectors? How well can your code be extended to such cases?
  
  
  
  
  
  
  
  
  
  
  
  
 Not sure about the implementation below but deque and popleft() should work. 
  
Solution:  
  
  class ZigzagIterator(object):

    def __init__(self, v1, v2):
        self.q = collections.deque([(len(v), iter(v)) for v in (v1, v2) if v])

    def next(self):
        len, iter = self.q.popleft()
        if len > 1:
            self.q.append((len-1, iter))
        return next(iter)

    def hasNext(self):
        return bool(self.q)

