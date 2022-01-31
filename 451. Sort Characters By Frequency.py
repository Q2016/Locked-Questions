Question:
Given a string s, sort it in decreasing order based on the frequency of the characters. The frequency of a character is the number 
of times it appears in the string. Return the sorted string. If there are multiple answers, return any of them.

Example 1:
Input: s = "tree"
Output: "eert"
Explanation: 'e' appears twice while 'r' and 't' both appear once.
So 'e' must appear before both 'r' and 't'. Therefore "eetr" is also a valid answer.    


Solution:

    def frequencySort(self, s):

        freq = collections.defaultdict(int)
        for c in s:
            freq[c] += 1
            
        counts = [""] * (len(s)+1)
        for c in freq:
            counts[freq[c]] += c
            
        result = ""
        for count in reversed(xrange(len(counts)-1)):
            for c in counts[count]:
                result += c * count
        
        return result

    
# Time:  O(n)
# Space: O(n)    
