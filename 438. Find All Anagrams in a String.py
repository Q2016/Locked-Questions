Question:
Given a string s and a non-empty string p, find all the start indices of p's anagrams in s. Strings consists of lowercase 
English letters only and the length of

Example 1:
Input: s: "cbaebabacd" p: "abc", Output: [0, 6]
Explanation:
The substring with start index = 0 is "cba", which is an anagram of "abc".
The substring with start index = 6 is "bac", which is an anagram of "abc".








Solution: Two pointers
    
    https://www.youtube.com/watch?v=G8xtZy0fDKg
  
class Solution:
    def findAnagrams(self, s, p):
        if len(p)>len(q): return []
        
        pCount, sCount={}, {}
        for i in range(len(p)):
            pCount[p[i]]=1+pCount.get(p[i],0)
            sCount[s[i]]=1+sCount.get(s[i],0)
            
        res=[0] if sCount==pCount else []
        l=0
        for r in range(len(p), len(s)):
            sCount[s[r]]=1+sCount.get(s[r],0)
            sCoount[s[l]] -=1
            
            if sCount[s[l]]==0: # not trivial
                sCount.pop(s[l])
                
            l+=1
            if sCount==pCount:
                res.append(l)
                
        return res 
            





    def findAnagrams(self, s, p):

        result = []
        cnts = [0] * 26
        for c in p:
            cnts[ord(c) - ord('a')] += 1
        
        left, right = 0, 0
        while right < len(s):
            cnts[ord(s[right]) - ord('a')] -= 1
            while left <= right and cnts[ord(s[right]) - ord('a')] < 0:
                cnts[ord(s[left]) - ord('a')] += 1
                left += 1
            if right - left + 1 == len(p):
                result.append(left)
            right += 1

        return result
    
    
# Time:  O(n)
# Space: O(1)    
