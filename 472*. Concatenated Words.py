Question:
Given an array of strings words (without duplicates), return all the concatenated words in the given list of words.
A concatenated word is defined as a string that is comprised entirely of at least two shorter words in the given array.

Example 1:
Input: words = ["cat","cats","catsdogcats","dog","dogcatsdog","hippopotamuses","rat","ratcatdogcat"]
Output: ["catsdogcats","dogcatsdog","ratcatdogcat"]
Explanation: "catsdogcats" can be concatenated by "cats", "dog" and "cats"; 
"dogcatsdog" can be concatenated by "dog", "cats" and "dog"; 
"ratcatdogcat" can be concatenated by "rat", "cat", "dog" and "cat".








Solution: 
  
https://www.youtube.com/watch?v=Wl4ylFY9BV8    
    
    
    
    
    
    
    
    
    
    
    
    
(similar to 139.)    
    
Do you still remember how did you solve this problem? https://leetcode.com/problems/word-break/

If you do know one optimized solution for above question is using DP, this problem is just one more step further. We iterate through each word 
and see if it can be formed by using other words.
Of course it is also obvious that a word can only be formed by words shorter than it. So we can first sort the input by length of each word, 
and only try to form one word by using words in front of it.    
    
class Solution(object):
    def findAllConcatenatedWordsInADict(self, words):

        d = set(words)
        
        def dfs(word):
            for i in range(1, len(word)):
                prefix = word[:i]
                suffix = word[i:]
                
                if prefix in d and suffix in d:
                    return True
                if prefix in d and dfs(suffix):
                    return True
                if suffix in d and dfs(prefix):
                    return True
            
            return False
        
        res = []
        for word in words:
            if dfs(word):
                res.append(word)
        
        return res
