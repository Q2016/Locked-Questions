Question:
Given a string s, return the longest palindromic substring in s.

Example 1:
Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.

    
    
    
    
    
    
    
    
    
    
Starting from a center char expands both ways to find palindrom substring    
    
Solution: Dynamic Programming
    
https://www.youtube.com/watch?v=XYQecbcd6_c
    
class Solution:
    def longestPalindrome(self, s):
        res=""
        resLen=0
        
        for i in range(len(s)):
            # odd length
            l,r=i,i
            while l>=0 and r <len(s) and s[l]==s[r]:
                if (r-l+1)>resLen:
                    res=s[l:r+1]
                    resLen=r-l+1
                l-=1
                r+=1
            # even length
            l,r=i,i+1
            while l>=0 and r<len(s) and s[l]==s[r]:
                if (r-l+1)>resLen:
                    res=s[l:r+1]
                    resLen=r-l+1
                l -=1
                r+=1
        
        return res
                



Time Complexity - O(N^2), 
Space Complexity - O(N^2)
