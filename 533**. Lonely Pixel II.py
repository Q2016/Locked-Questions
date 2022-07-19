Question:
Given a picture consisting of black and white pixels, and a positive integer N, find the number 
of black pixels located at some specific row R and column C that align with all the following rules:
Row R and column C both contain exactly N black pixels.
For all rows that have a black pixel at column C, they should be exactly the same as row R
The picture is represented by a 2D char array consisting of 'B' and 'W', which means black and 
white pixels respectively.

Example:
N = 3
Output: 6
Explanation: All the bold 'B' are the black pixels we need (all 'B's at column 1 and 3).
        0    1    2    3    4    5         column index                                            
0    [['W', 'B', 'W', 'B', 'B', 'W'],    
1     ['W', 'B', 'W', 'B', 'B', 'W'],    
2     ['W', 'B', 'W', 'B', 'B', 'W'],    
3     ['W', 'W', 'B', 'W', 'B', 'W']]    
row index

Take 'B' at row R = 0 and column C = 1 as an example:
Rule 1, row R = 0 and column C = 1 both have exactly N = 3 black pixels. 
Rule 2, the rows have black pixel at column C = 1 are row 0, row 1 and row 2. They are exactly the same as row R = 0.










No link

Solution:
Instead of MAP with two List, RowCountMap [N] indicates the number of rows having n 'b' plaids, and colcount [i] represents 
the number of 'b' lattice having the column. n ^ 2 Trailed to initialize these two Lists, then compare the MAP according to 
colcount, if value is not 0, the description is found, accumulating the number. 

def lonelyPixel2(self, grid):
    rows, cols = len(grid), len(grid[0])
    rowCountMap = colCount = [0 for i in range(cols)]
    for i in range(rows):
        rowCount = 0
        for j in range(cols):
            if grid[i][j] == 'W': continue
            rowCount += 1
            colCount[j] += 1
        rowCountMap[rowCount] += 1

    count = 0
    for blackCount in colCount:
        count += rowCountMap[count]
    return count

 
 
