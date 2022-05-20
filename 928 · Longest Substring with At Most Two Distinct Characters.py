Description
Given a string, find the length of the longest substring T that contains at most 2 distinct characters.

Example
Example 1
Input: “eceba”
Output: 3
Explanation:
T is "ece" which its length is 3.
Example 2
Input: “aaa”
Output: 3
  
  
  
  
  
  
  
Solution: Sliding window

class Solution:

    def lengthOfLongestSubstringTwoDistinct(self, s):
        longest, L, distinct_count, visited = 0, 0, 0, [0 for _ in xrange(256)]
        for R, char in enumerate(s):
            if visited[ord(char)] == 0:
                distinct_count += 1
            visited[ord(char)] += 1
            
            while distinct_count > 2:
                visited[ord(s[L])] -= 1
                if visited[ord(s[L])] == 0:
                    distinct_count -= 1
                L += 1
  
            longest = max(longest, R - L + 1)
        return longest

  
  
