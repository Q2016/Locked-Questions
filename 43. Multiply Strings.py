Question:
Given two non-negative integers num1 and num2 represented as strings, return the product of num1 and num2, also represented as a string.
Note: You must not use any built-in BigInteger library or convert the inputs to integer directly.

Example 1:
Input: num1 = "2", num2 = "3"
Output: "6"  

  
  
  
  
  
  
  
  
  
Elemntary school multiplication

Solution:

https://www.youtube.com/watch?v=1vZswirL8Y8
  
class Solution:
  def multiply(self, num1, num2):
    if "0" in [num1, num2]:
      return "0"
    
    res=[0]*(len(num1)+len(num2))
    num1, num2=num[::-1], num2[::-1]
    
    for i1 in range(len(num1)):
      for i2 in range(len(num2)):
        digit=int(num1[i1])*int(num2[i2])
        res[i1+i2]+=digit
        res[i1+i2]+=(res[i1+i2]%10)
        res[i1+i2+1]+=(res[i1+i2]//10)
        
    res,beg=res[::-1], 0
    while beg <len(res) and res[beg]==0:
      beg+=1
      
    res=map(str, res[beg:])
    return "".join(res)
    
  
  
  
  
  
  
  
  
      
Complexity Analysis

Here N and M are the number of digits in num1 and num2 respectively.
Time complexity: O(M⋅N).
During multiplication, we perform N operations for each of the M digits of the second number, so we need M⋅N time for it.
Space complexity: O(M+N).      
