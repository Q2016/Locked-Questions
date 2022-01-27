Question:
The DNA sequence is composed of a series of nucleotides abbreviated as 'A', 'C', 'G', and 'T'.
For example, "ACGAATTCCG" is a DNA sequence. When studying DNA, it is useful to identify repeated 
sequences within the DNA. Given a string s that represents a DNA sequence, return all the 10-letter-long 
sequences (substrings) that occur more than once in a DNA molecule. You may return the answer in any order.

Example 1:
Input: s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
Output: ["AAAAACCCCC","CCCCCAAAAA"]        

        
Solution:
I use a defauldict to initialize as 0 the dictionary of integers, then I check the dictionary for substrings seen more than once.

    def findRepeatedDnaSequences(self, s):
        sequences = collections.defaultdict(int)                              #set '0' as the default value for non-existing keys
        for i in range(len(s)):
            sequences[s[i:i+10]] += 1#add 1 to the count
        return [key for key, value in sequences.iteritems() if value > 1]     #extract the relevant keys        
