Question:
The power of an integer x is defined as the number of steps needed to transform x into 1 using the following steps:
if x is even then x = x / 2
if x is odd then x = 3 * x + 1
For example, the power of x = 3 is 7 because 3 needs 7 steps to become 1 (3 --> 10 --> 5 --> 16 --> 8 --> 4 --> 2 --> 1).
Given three integers lo, hi and k. The task is to sort all integers in the interval [lo, hi] by the power value in ascending order, 
if two or more integers have the same power value sort them by ascending order.
Return the kth integer in the range [lo, hi] sorted by the power value.

Example 1:
Input: lo = 12, hi = 15, k = 2
Output: 13
Explanation: The power of 12 is 9 (12 --> 6 --> 3 --> 10 --> 5 --> 16 --> 8 --> 4 --> 2 --> 1)
The power of 13 is 9
The power of 14 is 17
The power of 15 is 17
The interval sorted by the power value [12,13,14,15]. For k = 2 answer is the second element which is 13.
Notice that 12 and 13 have the same power value and we sorted them in ascending order. Same for 14 and 15.	



Solution: Brute force

import heapq
class Solution:
    def power(self,n):
        if n in self.dic:
            return self.dic[n]
        if n % 2:
            self.dic[n] = self.power(3 * n + 1) + 1
        else:
            self.dic[n] = self.power(n // 2) + 1
        return self.dic[n]    
    def getKth(self, lo: int, hi: int, k: int) -> int:
        self.dic = {1:0}
        for i in range(lo,hi+1):
            self.power(i)
                        
        lst = [(self.dic[i],i) for i in range(lo,hi+1)]
        heapq.heapify(lst)
        
        for i in range(k):
            ans = heapq.heappop(lst)
        
        return ans[1] 
