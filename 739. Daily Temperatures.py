Question:
Given an array of integers temperatures represents the daily temperatures, return an array answer such that answer[i] is the number of 
days you have to wait after the ith day to get a warmer temperature. If there is no future day for which this is possible, keep 
answer[i] == 0 instead.

Example 1:
Input: temperatures = [73,74,75,71,69,72,76,73]
Output: [1,1,4,2,1,1,0,0]

    
Solution:
    
Monotonic Stack: A monotonic stack is simply a stack where the elements are always in sorted order.    

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        answer = [0] * n
        stack = []
        
        for curr_day, curr_temp in enumerate(temperatures):
            # Pop until the current day's temperature is not
            # warmer than the temperature at the top of the stack
            while stack and temperatures[stack[-1]] < curr_temp:
                prev_day = stack.pop()
                answer[prev_day] = curr_day - prev_day
            stack.append(curr_day)
        
        return answer

Time complexity: O(N)

At first glance, it may look like the time complexity of this algorithm should be O(N^2), because there is a nested while loop inside the for loop. 
However, each element can only be added to the stack once, which means the stack is limited to N pops. Every iteration of the while loop uses 1 pop, 
which means the while loop will not iterate more than N times in total, across all iterations of the for loop.
An easier way to think about this is that in the worst case, every element will be pushed and popped once. This gives a time complexity of 
O(2N) = O(N).

Space complexity: O(N)
If the input was non-increasing, then no element would ever be popped from the stack, and the stack would grow to a size of N elements at the end.    
    
    
    
Time:  O(n)
Space: O(n)    
