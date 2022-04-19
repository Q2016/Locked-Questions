Question:
Given a string s and a string array dictionary, return the longest string in the dictionary that can be formed by deleting 
some of the given string characters. If there is more than one possible result, return the longest word with the smallest 
lexicographical order. If there is no possible result, return the empty string.

Example 1:
Input: s = "abpcplea", dictionary = ["ale","apple","monkey","plea"]
Output: "apple"    

    
    
    
    
    
    
    
    
    
Solution: Sort

If n is the length of our input string, m the length of our dictionary and w the average length of word in the dictionary, 
then we sort the dictionary at the cost of mlog m (len() costs O(1) in Python). We then iterate over each word additional m times. 
For each of those we check w * n times with early termination possibility. So in the worst case, this looks like it will be 
O(max(m * w * n, m log m)).

    def findLongestWord(self, s, d):

        d.sort(key = lambda x: (-len(x), x))
        for word in d:
            i = 0
            for c in s:
                if i < len(word) and word[i] == c:
                    i += 1
            if i == len(word):
                return word
        return ""
    
    
If our dictionary is very long but full of short words with a short input string 
then the sorting cost might outweigh the cost of the loop operations. If our words 
are very long but the dictionary is short, then the cost of the operations inside 
the loop will outweigh the cost of sort.    
# Time:  O((d * l) * logd), l is the average length of words
# Space: O(1)    
