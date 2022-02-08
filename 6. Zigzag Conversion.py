Question:
The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: 
P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR". Write the code that will take a string and make this conversion given a number of rows.
 

Example 1:
Input: s = "PAYPALISHIRING", numRows = 3
Output: "PAHNAPLSIIGYIR"
    
    
Solution:
    
    def convert(self, s, numRows):
        if numRows == 1:
            return s
        step, zigzag = 2 * numRows - 2, ""
        for i in xrange(numRows):
            for j in xrange(i, len(s), step):
                zigzag += s[j]
                if 0 < i < numRows - 1 and j + step - 2 * i < len(s):
                    zigzag += s[j + step - 2 * i]
        return zigzag
