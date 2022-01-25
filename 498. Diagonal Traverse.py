Question:
Given an m x n matrix mat, return an array of all the elements of the array in a diagonal order.    

Example1:    
Input: mat = [[1,2,3],
              [4,5,6],
              [7,8,9]]
Output: [1,2,4,7,5,3,6,8,9]
    
    
    
Solution: Dictionary 

The key here is to realize that the sum of indices on all diagonals are equal.
SO, if you can loop through the matrix, store each element by the sum of its indices 
in a dictionary, you have a collection of all elements on shared diagonals.
The last part is easy, build your answer (a list) by elements on diagonals. 
To capture the 'zig zag' or 'snake' phenomena of this problem, simply reverse over 
other diagonal level. So check if the level is divisible by 2.


def findDiagonalOrder(self, matrix: List[List[int]]) -> List[int]:
    d= collections.defaultdict(list)
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            d[i+j].append(matrix[i][j])
    ans= []
    for entry in d.items():
        if entry[0] % 2 == 0:
            ans.extend(entry[1][::-1])
        else:
            ans.extend(entry[1])
    return ans
