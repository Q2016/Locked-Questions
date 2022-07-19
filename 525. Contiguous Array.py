Question:
Given a binary array nums, return the maximum length of a contiguous subarray with an equal number of 0 and 1.

Example 2:
Input: nums = [0,1,0]
Output: 2
Explanation: [0, 1] (or [1, 0]) is a longest contiguous subarray with equal number of 0 and 1.    

  
  
  
  
  
  
  
  
  
  
  
  
  
No link  
  
Solution:

 0    \
-1      \
-2--------\-----/------   Example: [0, 0, 0, 0, 1, 1]
-3          \ /
-4   
     0 1 2 3 4 5 6
My thought was inspired by 121. Best Time to Buy and Sell Stock.
Let's have a variable count initially equals 0 and traverse through nums. Every time we meet a 0, we decrease count by 1, and increase count by 1 
when we meet 1. It's pretty easy to conclude that we have a contiguous subarray with equal number of 0 and 1 when count equals 0.
What if we have a sequence [0, 0, 0, 0, 1, 1]? the maximum length is 4, the count starting from 0, will equal -1, -2, -3, -4, -3, -2, and won't go back
to 0 again. But wait, the longest subarray with equal number of 0 and 1 started and ended when count equals -2. We can plot the changes of count on a graph, 
as shown above. Point (0,0) indicates the initial value of count is 0, so we count the sequence starting from index 1. The longest subarray is from index 2 to 6.
From above illustration, we can easily understand that two points with the same y-axis value indicates the sequence between these two points has 
equal number of 0 and 1.
To find the maximum length, we need a dict to store the value of count (as the key) and its associated index (as the value). 
We only need to save a count value and its index at the first time, when the same count values appear again, we use the new index 
subtracting the old index to calculate the length of a subarray. A variable max_length is used to to keep track of the current maximum length.

    def findMaxLength(self, nums):
        count = 0
        max_length=0
        table = {0: 0}
        for index, num in enumerate(nums, 1):
            if num == 0:
                count -= 1
            else:
                count += 1
            
            if count in table:
                max_length = max(max_length, index - table[count])
            else:
                table[count] = index
        
        return max_length

Time O(n)      
