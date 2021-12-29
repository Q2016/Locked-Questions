https://leetcode.com/problems/image-overlap/solution/



Approach 2: Linear Transformation
Intuition

One drawback of the above algorithm is that we would scan through those
zones that are filled with zeros over and over, even though these zones are not of our interests.

Because for those cells filled with zero, no matter how we shift, they would
not add up to the final solutions. As a follow-up question, we could ask 
ourselves that, can we focus on those cells with ones?

The answer is yes. The idea is that we filter out those cells with ones in
both matrices, and then we apply the linear transformation to align the cells.

First of all, we define a 2-dimension coordinate, via which we could assign a unique 
coordinate to each cell in the matrix, e.g. a cell can be indexed as I = (X_i, Y_i).

Then to shift a cell, we can obtain the new position of the cell by applying a 
linear transformation. For example, to shift the cell to the right by one and 
to the up side by one is to apply the linear transformation vector of V = (1, 1). 
The new index of the cell can be obtained by I + V = (X_i + 1, Y_i + 1).

Furthermore, given two matrices, we have two non-zero cells respectively in 
the matrices as P_a =(X_a, Y_a) and P_b = (X_b, Y_b). To align these cells 
together, we would need a transformation vector as V_{ab} = (X_b - X_a, Y_b - Y_a), 
so that P_a + V_{ab} = P_b.

Now, the key insight is that all the cells in the same overlapping zone would 
share the same linear transformation vector.

Based on the above insight, we can then use the transformation vector V_{ab} 
as a key to group all the non-zero cells alignments between two matrices. 
Each group represents an overlapping zone. Naturally, the size of the 
overlapping zone would be the size of the group as well.

Algorithm

The algorithm can be implemented in two overall steps.

First, we filter out those non-zero cells in each matrix respectively.

Second, we do a cartesian product on the non-zero cells. For each pair of the products, 
we calculate the corresponding linear transformation vector as V_{ab} = (X_b - X_a, Y_b - Y_a). 
Then, we count the number of the pairs that have the same transformation vector, which 
is also the number of ones in the overlapping zone.


class Solution:
    def largestOverlap(self, A: List[List[int]], B: List[List[int]]) -> int:

        dim = len(A)

        def non_zero_cells(M):
            ret = []
            for x in range(dim):
                for y in range(dim):
                    if M[x][y] == 1:
                        ret.append((x, y))
            return ret

        transformation_count = defaultdict(int)
        max_overlaps = 0

        A_ones = non_zero_cells(A)
        B_ones = non_zero_cells(B)

        for (x_a, y_a) in A_ones:
            for (x_b, y_b) in B_ones:
                vec = (x_b - x_a, y_b - y_a)
                transformation_count[vec] += 1
                max_overlaps = max(max_overlaps, transformation_count[vec])

        return max_overlaps
        
        
        
Complexity Analysis

Let M_a, M_b be the number of non-zero cells in the matrix A and B respectively. Let NN be the width of the matrix.

Time Complexity: O(N^4).

In the first step, we filter out the non-zero cells in each matrix, which would take O(N^2) time.
In the second step, we enumerate the cartesian product of non-zero cells between 
the two matrices, which would take O(M_a.M_b) time. In the worst case, 
both M_a and M_b would be up to N^2, i.e. matrix filled with ones.

To sum up, the overall time complexity of the algorithm would be O(N2)+O(N 2⋅N 2)=O(N4).

Although this approach has the same time complexity as the previous approach, it should 
run faster in practice, since we ignore those zero cells.

Space Complexity: O(N^2) We kept the indices of non-zero cells in both matrices. In the 
worst case, we would need the O(N2) space for the matrices filled with ones.
