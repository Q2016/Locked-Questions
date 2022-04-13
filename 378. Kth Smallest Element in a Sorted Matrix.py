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



Solution: Binary Search
  
We are done here, but let's think about this problem in another way:
The key point for any binary search is to figure out the "Search Space". For me, I think there are two kind of "Search Space" -- index and 
range(the range from the smallest number to the biggest number). Most usually, when the array is sorted in one direction, we can use index as 
"search space", when the array is unsorted and we are going to find a specific number, we can use "range".

Let me give you two examples of these two "search space"

index -- A bunch of examples -- https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/ ( the array is sorted)
range -- https://leetcode.com/problems/find-the-duplicate-number/ (Unsorted Array)
The reason why we did not use index as "search space" for this problem is the matrix is sorted in two directions, we can not find a linear way 
to map the number and its index.

public class Solution {
    public int kthSmallest(int[][] matrix, int k) {
        int lo = matrix[0][0], hi = matrix[matrix.length - 1][matrix[0].length - 1] + 1;//[lo, hi)
        while(lo < hi) {
            int mid = lo + (hi - lo) / 2;
            int count = 0,  j = matrix[0].length - 1;
            for(int i = 0; i < matrix.length; i++) {
                while(j >= 0 && matrix[i][j] > mid) j--;
                count += (j + 1);
            }
            if(count < k) lo = mid + 1;
            else hi = mid;
        }
        return lo;
    }
}
