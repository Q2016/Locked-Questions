Question:
Design a hit counter which counts the number of hits received in the past 5 minutes. Each function accepts a timestamp 
parameter (in seconds granularity) and you may assume that calls are being made to the system in chronological order 
(ie, the timestamp is monotonically increasing). You may assume that the earliest timestamp starts at 1. It is possible 
that several hits arrive roughly at the same time.

Example:
HitCounter counter = new HitCounter();
// hit at timestamp 1.
counter.hit(1);
// hit at timestamp 2.
counter.hit(2);
// hit at timestamp 3.
counter.hit(3);
// get hits at timestamp 4, should return 3.
counter.getHits(4);
// hit at timestamp 300.
counter.hit(300);
// get hits at timestamp 300, should return 4.
counter.getHits(300);
// get hits at timestamp 301, should return 3.
counter.getHits(301);
Follow up: What if the number of hits per second could be very large? Does your design scale?
  
  
  
  
  
  
  
  
  
  
  
  
  
  
The fact that we need to keep data for 5min is a hint for deque.  
 
Solution:  
https://www.youtube.com/watch?v=WkLuQeVsXtY
  
uses a bucket  
  
class HitCounter(object):

    def __init__(self):
      self.time=[0]*300
      self.count=[0]*300

    def hit(self, timestamp):
      index=timestamp % 300
      
      if self.time[index] != timestamp:
        self.time[index] = timestamp
        self.count[index] = 1
      else:
        self.count[index] += 1

    def getHits(self, timestamp):
      ans=0
      
      for i in range(300):
        if self.time[i] > timestamp - 300:
          ans += self.count[i]
          
      return ans
      
      

    
