Question:
Given a string S, find out the length of the longest repeating substring(s). Return 0 if no repeating substring exists.


Example 1:

Input: "abcd"
Output: 0
Explanation: There is no repeating substring.
Example 2:

Input: "abbaba"
Output: 2
Explanation: The longest repeating substrings are "ab" and "ba", each of which occurs twice.
Example 3:

Input: "aabcaabdaab"
Output: 3
Explanation: The longest repeating substring is "aab", which occurs 3 times.

  
  
Solution:
  
class Solution:
    def longestRepeatingSubstring(self, S: str) -> int:
        ans = 0
        for i in range(1, len(S)):
            if ans >= len(S)-i: 
                break 
                
            tmp = 0
            for x, y in zip(S[i:],S[:-i]):
                if x == y:
                    tmp += 1 
                    ans = max(ans, tmp)
                else:
                    tmp = 0 
            
        return ans
