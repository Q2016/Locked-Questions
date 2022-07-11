Question:
Given an n x n matrix where each of the rows and columns is sorted in ascending order, return the kth smallest element in the matrix.
Note that it is the kth smallest element in the sorted order, not the kth distinct element. You must find a solution with a memory 
complexity better than O(n^2).

Example 1:
Input: matrix = [[1, 5, 9 ],
                 [10,11,13],
                 [12,13,15]], k = 8
Output: 13
Explanation: The elements in the matrix are [1,5,9,10,11,12,13,13,15], and the 8th smallest number is 13    



  
  
  
  
The Priority Queue is the standart way of treating sorted matrix problem. The brute-force takes   O(n^2*log n^2)
  
Solution: Binary Search
  
 https://www.youtube.com/watch?v=IAj57xARMd4 
  
for each row of matrix, send first element to priorty Queue with index, it help when we pop, what's next element
that goes into queue 
  
  
def kthSmallest(self, matrix, k):
  n=len(matrix)
  pq=[]
  
  for j in range(min(n,k)):
    heapq.heappush(pq, (matrix[0][j],0,j))
    
  while k>1:
    num, i, j =heapq.heappop(pq)
    
    if i<n-1:
      heapq.heappush(pq, (matrix[i+1][j],i+1,j))
      
    k -=1
  
  return pq[0][0]
 
Time O(nlogn+klogn)    
  
  
  
Binary search:

def kthSmallest(self, matrix, k):
  
  
    def countLessOrEqualNums(mid):
        count=0

        for i in range(n):
          if matrix[i][0]>mid:
            break

          for j in range(n):
            if matrix[i][j]<=mid:
              count +=1
            else:
              break
      
        return count
    
    n=len(matrix)

    left=matrix[0][0]
    right=matrix[n-1][n-1]

    while left<right:
      mid =left+(right-left)//2

      if countLessOrEqualNums(mid)<k:
        left=mid+1
      else:
        right=mid

    return left

  
  
  
  
  

