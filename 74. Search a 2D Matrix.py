Question:
Write an efficient algorithm that searches for a value target in an m x n integer matrix. This matrix has the following properties:
Integers in each row are sorted from left to right.
The first integer of each row is greater than the last integer of the previous row.
 
Example 1:
Input: matrix = [[ 1, 3, 5, 7],
                 [10,11,16,20],
                 [23,30,34,60]], target = 3
Output: true    

    
  
  
  
  
  
  
  
  
Solution: BST (look at 'high', as if a long 1d array, interesting how 'mid' is used)
It is basically an advanced version of the binary search

class Solution:

    def searchMatrix(self, matrix, target):
        if not matrix or target is None:
            return False

        rows, cols = len(matrix), len(matrix[0])
        low, high = 0, rows * cols - 1
        
        while low <= high:
            mid = (low + high) / 2
            num = matrix[mid / cols][mid % cols]

            if num == target:
                return True
            elif num < target:
                low = mid + 1
            else:
                high = mid - 1
        
        return False    
