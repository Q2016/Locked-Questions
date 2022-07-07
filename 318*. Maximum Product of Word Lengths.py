Question:
Given a string array words, return the maximum value of length(word[i]) * length(word[j]) where the two words do not share common letters. 
If no such two words exist, return 0.

Example 1:
Input: words = ["abcw","baz","foo","bar","xtfn","abcdef"]
Output: 16
Explanation: The two words can be "abcw", "xtfn".

	
	
	
	
	
	
	
	
	
	
Solution:

https://www.youtube.com/watch?v=dE88fgc73jQ

class Solution(object):
    
    def maxProduct(self, words):
	masks=[]
	for word in words:
	   mask=0
	   for c in word:
		bit=ord(c)-ord('a')
		mask |= 1<<bit  # i  dont understand this part (bit wise or) translate the corresponding number to bitmask
			
	   masks.append(mask)
	
	ans=0
	n=len(words)
	
	for i in range(n):
	   for j in range(n):
	       if i !=j:
		  if masks[i] &masks[j]==0:
			ans=max(ans, len(words[i])*len(words[j]))
	return ans

Time complexity O(n^2)
