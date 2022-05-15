Question:
In a string composed of 'L', 'R', and 'X' characters, like "RXXLRXRXL", a move consists of either replacing one occurrence of "XL" with "LX", 
or replacing one occurrence of "RX" with "XR". Given the starting string start and the ending string end, return True if and only if there 
exists a sequence of moves to transform one string to the other.

Example 1:
Input: start = "RXXLRXRXL", end = "XRLXXRRLX"
Output: true
Explanation: We can transform start to end following these steps:
RXXLRXRXL ->XRXLRXRXL ->XRLXRXRXL ->XRLXXRRXL ->XRLXXRRLX    
    
    
Solution:    
for picture:
https://leetcode.com/problems/swap-adjacent-in-lr-string/discuss/873004/Easy-to-understand-explanation-with-PICTURE
	
Key observations:
There are three kinds of characters, ‘L’, ‘R’, ‘X’.
Replacing XL with LX = move L to the left by one
Replacing RX with XR = move R to the right by one
If we remove all the X in both strings, the resulting strings should be the same.

Additional observations:
Since a move always involves X, an L or R cannot move through another L or R.
Since an L can only move to the right, for each occurrence of L in the start string, its position should be to the same or to the left of 
its corresponding L in the end string.

Implementation
We first compare two strings with X removed. This checks relative position between Ls and Rs are correct.

Then we find the indices for each occurence of L and check the condition in the above figure. Then we do the same for R.

class Solution:
    def canTransform(self, start: str, end: str) -> bool:
        if len(start) != len(end): return False
        
        # check L R orders are the same
        if start.replace('X','') != end.replace('X', ''): return False
        
        n = len(start)
        Lstart = [i for i in range(n) if start[i] == 'L']
        Lend = [i for i in range(n) if end[i] == 'L']
        
        Rstart = [i for i in range(n) if start[i] == 'R']
        Rend = [i for i in range(n) if end[i] == 'R']
		# check L positions are correct
        for i, j in zip(Lstart, Lend):
            if i < j:
                return False
            
        # check R positions are correct
        for i, j in zip(Rstart, Rend):
            if i > j:
                return False
            
        return True
