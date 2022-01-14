Solution from to see the images:
  https://leetcode.com/problems/count-submatrices-with-all-ones/discuss/720265/Java-Detailed-Explanation-From-O(MNM)-to-O(MN)-by-using-Stack
    
Similar questions:
https://leetcode.com/problems/maximal-rectangle/
https://leetcode.com/problems/largest-rectangle-in-histogram  
    
    
O(M * N * M):
Imagine you have an one-dimension array, how to count number of all 1 submatrices (size is 1 * X). It's pretty simple right?

int res = 0, length = 0;
for (int i = 0; i < A.length; ++i) {
	length = (A[i] == 0 ? 0 : length + 1);
	res += length;
}
return res;
Now, Let's solve 2D matrix by finding all 1 submatrices from row "up" to row "down". And apply above 1D helper function. Note: the array h[k] == 1 means all values in column k from row "up" to "down" are 1 (that's why we use &). So overall, the idea is to "compress" the 2D array to the 1D array, and apply 1D array method on it, while trying all heights up to down.

public int numSubmat(int[][] mat) {
        
	int M = mat.length, N = mat[0].length;

	int res = 0;
	for (int up = 0; up < M; ++up) {
		int[] h = new int[N];
		Arrays.fill(h, 1);
		for (int down = up; down < M; ++down) {
			for (int k = 0; k < N; ++k) h[k] &= mat[down][k];
			res += countOneRow(h);
		}
	}

	return res;
}

private int countOneRow(int[] A) {

	int res = 0, length = 0;
	for (int i = 0; i < A.length; ++i) {
		length = (A[i] == 0 ? 0 : length + 1);
		res += length;
	}
	return res;
}
O(M * N) by Using Stack
Now in the code, the h[j] means: number of continius 1 in column j from row i up to row 0. By using mono-stack, what we want to achieve is to find the first previous index "preIndex", whose number of continuous 1 is less than current column index i. And the value of index between preIndex and i are all equal or larger than index i. So it can form a big sub-matrix.

Note: sum[i] means the number of submatrices with the column "i" as the right border.

If stack is empty, meaning: all previous columns has more/equal ones than current column. So, the number of matrixs can form is simply A[i] * (i + 1); (0-index)
If stack is not empty, meaning: there is a shorter column which breaks our road. Now, the number of matrixs can form is sum[i] += A[i] * (i - preIndex). And plus, we can form a longer submatrices with that previou shorter column sum[preIndex].
The best way to understand is to draw a graph.
image

public int numSubmat(int[][] mat) {
        
	int M = mat.length, N = mat[0].length;

	int res = 0;

	int[] h = new int[N];
	for (int i = 0; i < M; ++i) {
		for (int j = 0; j < N; ++j) {
			h[j] = (mat[i][j] == 0 ? 0 : h[j] + 1);
		}
		res += helper(h);
	}

	return res;
}

private int helper(int[] A) {

	int[] sum = new int[A.length];
	Stack<Integer> stack = new Stack<>();

	for (int i = 0; i < A.length; ++i) {

		while (!stack.isEmpty() && A[stack.peek()] >= A[i]) stack.pop();

		if (!stack.isEmpty()) {
			int preIndex = stack.peek();
			sum[i] = sum[preIndex];
			sum[i] += A[i] * (i - preIndex);
		} else {
			sum[i] = A[i] * (i + 1);
		}

		stack.push(i);
	}

	int res = 0;
	for (int s : sum) res += s;

	return res;
}    
