Question:
Given a string s, find the length of the longest substring without repeating characters.

Example 1:
Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring. <------- Diff between substring and subsequence   


    
    
    
    
    
    
    
    
    
Solution: Two Pointers
    
    https://www.youtube.com/watch?v=wiGpQwVHdE0
    
    def lengthOfLongestSubstring(self, s):
        charSet=set()
        l=0
        res=0
        
        for r in range(len(s)):
            while s[r] in charSet:
                charSet.remove(s[l])
                l+=1
            charSet.add(s[r])
            res=max(res, r-l+1)
         
        return res
            

Time:  O(n)
Space: O(n)    
