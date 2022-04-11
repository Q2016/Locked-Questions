Question:
Given a string array words, return the maximum value of length(word[i]) * length(word[j]) where the two words do not share common letters. 
If no such two words exist, return 0.

Example 1:
Input: words = ["abcw","baz","foo","bar","xtfn","abcdef"]
Output: 16
Explanation: The two words can be "abcw", "xtfn".

	
	
	
	
	
	
	
	
Solution:

Simple brute force solution is to test if every pair for similarity and take the product is they are not similar. Return the maximum product if 
several dissimilar pairs are found otherwise return 0.
First optimization is to run the two for loops from** i = (0 to N-1) and j = (i+1, N-1)**. This is lesser than N^2.
How do we find if two words are similar?

First approach will be to take two words, put all characters into a set and test for membership in that set for the other words. Can we do better? 
Can we pre-process somehow?
Second approach will be to prepprocess each word and generate a unique sign for it. Take a boolean array of 26. Mark the position for every 
character in this word as True. Now traverse this array in order and generate a unique signature. O(26 + len(word)). Can we still do better?
Can we use bit-wise manipulation? int32 is 32 bits. There are 26 letters. Set a bit for every character. How do you test if two words have no 
similar letters? Just AND them. Testing them now becomes a constant time operation

class Solution(object):
    def sign(self, word):
        value = 0
        for c in word:
            value = value | (1 << (ord(c)-97))
        return value
    
    def maxProduct(self, words):

        signature = [self.sign(x) for x in words]
        max_product, N = 0, len(words)
        for i in range(N):
            for j in range(i+1, N):
                if signature[i] & signature[j] == 0:
                    max_product = max(max_product, len(words[i])*len(words[j]))
        return max_product

Use set as a signature
Yes another way is to use sets in an interesting manner.

Use this for generating signatures: signature = {w:set(w) for w in words}
Use this for testing: bool(signature[words[i]] & signature[words[j]]) == False
https://docs.python.org/2/library/sets.html

class Solution(object):
    def maxProduct(self, words):

        signature = {w:set(w) for w in words}
        max_product, N = 0, len(words)
        for i in range(N):
            for j in range(i+1, N):
                # Intersection of two sets
                if bool(signature[words[i]] & signature[words[j]]) == False:
                    max_product = max(max_product, len(words[i])*len(words[j]))
        return max_product 
