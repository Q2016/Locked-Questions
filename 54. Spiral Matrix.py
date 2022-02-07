Question:
  
  
  
  
Solution:  
This is a very simple and easy to understand solution. I traverse right and increment rowBegin, then traverse 
down and decrement colEnd, then I traverse left and decrement rowEnd, and finally I traverse up and increment colBegin.
The only tricky part is that when I traverse left or up I have to check whether the row or col still exists to prevent duplicates. 


  def spiralOrder(self, matrix):
        if not matrix: return []
        
        row_start = 0
        row_end = len(matrix) - 1
        
        col_start = 0
        col_end = len(matrix[0]) - 1
        
        res = []
        while row_start <= row_end and col_start <= col_end:
            
            # right
            for j in range(col_start, col_end+1):
                res.append(matrix[row_start][j])
            row_start += 1
            
            # down
            for i in range(row_start, row_end+1):
                res.append(matrix[i][col_end])
            col_end -= 1
            
            # left
            if row_start <= row_end:
                for j in range(col_end, col_start-1, -1):
                    res.append(matrix[row_end][j])

                row_end -= 1

            # up
            if col_start <= col_end:
                for i in range(row_end, row_start-1, -1):
                    res.append(matrix[i][col_start])
                col_start += 1
         
        return res
