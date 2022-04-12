Question:
You are given two integer arrays nums1 and nums2 sorted in ascending order and an integer k. Define a pair (u, v) which consists of 
one element from the first array and one element from the second array. Return the k pairs (u1, v1), (u2, v2), ..., (uk, vk) with 
the smallest sums.

Example 1:
Input: nums1 = [1,7,11], nums2 = [2,4,6], k = 3
Output: [[1,2],[1,4],[1,6]]
Explanation: The first 3 pairs are returned from the sequence: [1,2],[1,4],[1,6],[7,2],[7,4],[11,2],[7,6],[11,4],[11,6]


		
		
		
		
		
		
		
Solution: BST or there is heap solution as well
	
It's helpful to visualize the input as an m×n matrix of sums, for example for nums1=[1,7,11], and nums2=[2,4,6]:
      2   4   6
   +------------
 1 |  3   5   7
 7 |  9  11  13
11 | 13  15  17
Of course the smallest pair overall is in the top left corner, the one with sum 3. We don't even need to look anywhere else. 
After including that pair in the output, the next-smaller pair must be the next on the right (sum=5) or the next below (sum=9).
We can keep a "horizon" of possible candidates, implemented as a heap / priority-queue, and roughly speaking we'll grow from the 
top left corner towards the right/bottom. 

Creating the matrix now it's 378. Kth Smallest Element in a Sorted Matrix problem.

Before we start this question, we should know how to solve question 378.
Before we start question 378, we should know how to work on question 23: merge two sorted Lists
For this question, we can translate it into matrix
e.g.: nums1 = [1,7,11], nums2 = [2,4,6], k = 3

		                1        7         11
                 2        1,2      7,2       11,2
		     4        1,4      7,4       11,4
		     6        1,6      7,6       11,6
Each row is sorted by sum and each column is sorted by sum. That's the same question of 378.

We use the same way of question 23 (which is also the same way of question 378):

PriorityQueue to save the first column.
poll one value, then push this value into result list.
Then, push the next value of that row into PriorityQueue.
	
	
public List<List<Integer>> kSmallestPairs(int[] nums1, int[] nums2, int k) {
        int cols = nums1.length, rows = nums2.length;

        List<List<Integer>> ans = new ArrayList<>();

        PriorityQueue<int[]> q = new PriorityQueue<>((a, b) -> a[0] - b[0]);

        for(int row = 0; row < rows; row++) q.add(new int[]{nums2[row] + nums1[0], row, 0}); // {value, row, col}

        while(!q.isEmpty()) {
            int[] val = q.poll();
            ans.add(new ArrayList<>(Arrays.asList(nums1[val[2]], nums2[val[1]])));
            k--;
            if(k == 0) return ans;

            val[2]++;
            if(val[2] == cols) continue;
            val[0] = nums1[val[2]] + nums2[val[1]];
            q.add(val);
        }

        return ans;
    }
