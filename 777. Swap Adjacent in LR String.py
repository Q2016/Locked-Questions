Question:
In a string composed of 'L', 'R', and 'X' characters, like "RXXLRXRXL", a move consists of either replacing one occurrence of "XL" with "LX", 
or replacing one occurrence of "RX" with "XR". Given the starting string start and the ending string end, return True if and only if there 
exists a sequence of moves to transform one string to the other.

Example 1:
Input: start = "RXXLRXRXL", end = "XRLXXRRLX"
Output: true
Explanation: We can transform start to end following these steps:
RXXLRXRXL ->
XRXLRXRXL ->
XRLXRXRXL ->
XRLXXRRXL ->
XRLXXRRLX    
    
    
Solution:    

class Solution(object):
    def canTransform(self, start, end):
        if len(start) != len(end): return False
        
        A = [(s, idx) for idx, s in enumerate(start) if s == 'L' or s == 'R']
        B = [(e, idx) for idx, e in enumerate(end) if e == 'L' or e == 'R']
        if len(A) != len(B): return False
        
        for (s, i), (e, j) in zip(A, B):
            if s != e: return False
            if s == 'L':
                if i < j:
                    return False
            if s == 'R':
                if i > j:
                    return False
            
        return True
