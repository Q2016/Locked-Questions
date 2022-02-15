Question:
Given an array of integers temperatures represents the daily temperatures, return an array answer such that answer[i] is the number of 
days you have to wait after the ith day to get a warmer temperature. If there is no future day for which this is possible, keep 
answer[i] == 0 instead.

Example 1:
Input: temperatures = [73,74,75,71,69,72,76,73]
Output: [1,1,4,2,1,1,0,0]

    
Solution:
lots of different approaches:
https://leetcode.com/problems/daily-temperatures/solution/

class Solution(object):
    def dailyTemperatures(self, temperatures):

        result = [0] * len(temperatures)
        stk = []
        for i in xrange(len(temperatures)):
            while stk and \
                  temperatures[stk[-1]] < temperatures[i]:
                idx = stk.pop()
                result[idx] = i-idx
            stk.append(i)
        return result 

    
Time:  O(n)
Space: O(n)    
