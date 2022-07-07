Question:
Given a string containing just the characters '(' and ')', find the length of the longest valid (well-formed) parentheses substring.

Example 1:
Input: s = "(()"
Output: 2
Explanation: The longest valid parentheses substring is "()".  
  

  
  
  
  

  
  
  
  
  
It's interesting to know that there's a DP solution to this problem as well.  
  
Solution: Stack

https://www.youtube.com/watch?v=OsmvjLStiqY

class Solution:
   def longest(s):
      stack=[-1]
      ans=0
      
      for i, c in enumerate(s):
          if c =='(':
              stack.append(i)
          else:
              if stack and stack[-1] !=-1 and s[stack[-1]] =='(':
                stack.pop()
                ans=max(ans, i-stack[-1])
              else:
                stack.append(i)
      
      return ans
