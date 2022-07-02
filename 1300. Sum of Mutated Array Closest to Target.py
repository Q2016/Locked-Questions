Question:
Given an integer array arr and a target value target, return the integer value such that 
when we change all the integers larger than value in the given array to be equal to value, 
the sum of the array gets as close as possible (in absolute difference) to target.
In case of a tie, return the minimum such integer.
    
Example 1:
Input: arr = [4,9,3], target = 10
Output: 3
Explanation: When using 3 arr converts to [3, 3, 3] which sums 9 and that's the optimal answer.

  








Solution: 
    
Just sort, I have also seen Binary Search  solution
    
    def findBestValue(self, A, target):
        A.sort(reverse=1)
        maxA = A[0]
        while A and target >= A[-1] * len(A):
            target -= A.pop()
        return int(round((target - 0.0001) / len(A))) if A else maxA

    
Time nlogn    
