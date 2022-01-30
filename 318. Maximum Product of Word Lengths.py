Question:
Given a string array words, return the maximum value of length(word[i]) * length(word[j]) where the two words do not share common letters. 
If no such two words exist, return 0.

Example 1:
Input: words = ["abcw","baz","foo","bar","xtfn","abcdef"]
Output: 16
Explanation: The two words can be "abcw", "xtfn".

	
Solution:

Straightforward solution is to compare each pair of words. We can use the fact that each word has only letters from a to z and for 
each word what is matter if it has some letter or not. Let d[word] be bitmask of word. For example for word aaabe we will have 
mask ...10011, here I for simplicity show only the last part, all other elements are zero. We have 1 in the end, because we have 
a in our word, we have 1 as next elements, because we have b, then we have 0, because we do not have c and so on. So, the whole 
algorithm can be separated into two stages:
Compute all masks for all words, we will use d[word] |= 1<<(ord(l) - 97) for this, where 97 is code of symbol a. 
Also we use | (or) here to update zero-elements, but if we have one-elements, they will not change.
For every pair of words check if d[w1] & d[w2] == 0, this is condition that pair of words will not have any intersections 
and update our ans if they not.

    def maxProduct(self, words):
        d, ans = defaultdict(int), 0
        for word in words:
            for l in word:
                d[word] |= 1<<(ord(l) - 97)
                
        for w1, w2 in combinations(d.keys(), 2):
            if d[w1] & d[w2] == 0: 
                ans = max(ans, len(w1)*len(w2))            
        return ans	


Compexity
Time complexity is O(n*s) + O(n^2), where s is the average length of word and n is number of words. Space complexity is O(n).
