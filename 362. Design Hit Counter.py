Design a hit counter which counts the number of hits received in the past 5 minutes.

Each function accepts a timestamp parameter (in seconds granularity) and you may assume that calls are being made to the system in chronological order (ie, the timestamp is monotonically increasing). You may assume that the earliest timestamp starts at 1.

It is possible that several hits arrive roughly at the same time.

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
  
  
  
  
 https://github.com/ShiqinHuo/LeetCode-Python/blob/master/Python/design-hit-counter.py 
  
# Time:  O(1), amortized
# Space: O(k), k is the count of seconds.

from collections import deque

class HitCounter(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.__k = 300
        self.__dq = deque()
        self.__count = 0

    def hit(self, timestamp):
        """
        Record a hit.
        @param timestamp - The current timestamp (in seconds granularity).
        :type timestamp: int
        :rtype: void
        """
        self.getHits(timestamp)
        if self.__dq and self.__dq[-1][0] == timestamp:
            self.__dq[-1][1] += 1
        else:
            self.__dq.append([timestamp, 1])
        self.__count += 1

    def getHits(self, timestamp):
        """
        Return the number of hits in the past 5 minutes.
        @param timestamp - The current timestamp (in seconds granularity).
        :type timestamp: int
        :rtype: int
        """
        while self.__dq and self.__dq[0][0] <= timestamp - self.__k:
            self.__count -= self.__dq.popleft()[1]
        return self.__count

# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)
