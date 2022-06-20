Question:
Given a string s, find the length of the longest substring without repeating characters.

Example 1:
Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring. <------- Diff between substring and subsequence   


    
    
    
    
    
    
    
    
    
Solution: Two Pointers
    
    def lengthOfLongestSubstring(self, s):
        start = maxLength = 0
        usedChar = {}
        
        for i in range(len(s)):
            if s[i] in usedChar and start <= usedChar[s[i]]:
                start = usedChar[s[i]] + 1
            else:
                maxLength = max(maxLength, i - start + 1)

            usedChar[s[i]] = i

        return maxLength


    
# Time:  O(n)
# Space: O(1)    
