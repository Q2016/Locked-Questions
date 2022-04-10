Question:
Write an efficient algorithm that searches for a value target in an m x n integer matrix matrix. 
This matrix has the following properties: Integers in each row are sorted in ascending from left to right.
Integers in each column are sorted in ascending from top to bottom.
 
Example 1:
Input: matrix = [[1, 4, 7, 11,15],
		 [2, 5, 8, 12,19],
		 [3, 6, 9, 16,22],
		 [10,13,14,17,24],
		 [18,21,23,26,30]], target = 5
Output: true

	


	
	
Solutions: Binary search

Take advantage of the property with sorted ordering in row and column respectively.
First, use range check to locate possible candidate row. Second, launch 1D binary search on each possible candidate row.


    def searchMatrix(self, matrix: List[List[int]], target: int)-> bool:
               
        if not len(matrix) or not len(matrix[0]):
            # Quick response for empty matrix
            return False
        
        h, w = len(matrix), len(matrix[0]) 
        for row in matrix:
	# range check
            if row[0] <= target <= row[-1]:        
		# launch binary search on current possible row		
                left, right = 0, w-1
                while left <= right:
                    mid = left + (right - left) // 2
                    mid_value = row[mid]
                    if target > mid_value:
                        left = mid+1
                    elif target < mid_value:
                        right = mid-1
                    else:
                        return True
        return False


Complexity: O(mlog n)
